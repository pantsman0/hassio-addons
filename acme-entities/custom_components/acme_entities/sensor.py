"""Sensor platform for ACME Entities."""

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import callback
from homeassistant.helpers.dispatcher import (
    async_dispatcher_connect,
    async_dispatcher_send,
)

from .const import DOMAIN, EVENT_STATUS

SIGNAL_UPDATE = f"{DOMAIN}_update"


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the sensor platform."""
    known_certs = set()

    @callback
    def handle_event(event):
        cert_name = event.data.get("name")
        if not cert_name:
            return

        if cert_name not in known_certs:
            known_certs.add(cert_name)
            async_add_entities([AcmeCertificateSensor(cert_name, event.data)])
        else:
            async_dispatcher_send(hass, f"{SIGNAL_UPDATE}_{cert_name}", event.data)

    hass.bus.async_listen(EVENT_STATUS, handle_event)


class AcmeCertificateSensor(SensorEntity):
    """Representation of an ACME Certificate Sensor."""

    def __init__(self, name, data):
        self._name = name
        self._attr_name = f"ACME Certificate - {name}"
        self._attr_unique_id = (
            f"acme_cert_{name.replace('.', '_').replace('*', 'wildcard')}"
        )
        self._attr_icon = "mdi:certificate"
        self._update_data(data)

    def _update_data(self, data):
        self._attr_native_value = data.get("state")

        attributes = data.get("attributes", {})
        self._attr_extra_state_attributes = {
            "domains": attributes.get("domains"),
            "certfile": attributes.get("certfile"),
            "keyfile": attributes.get("keyfile"),
            "expiry": attributes.get("expiry"),
            "days_remaining": attributes.get("days_remaining"),
        }
        if "error" in attributes:
            self._attr_extra_state_attributes["error"] = attributes["error"]

    async def async_added_to_hass(self):
        """Run when entity about to be added to hass."""
        self.async_on_remove(
            async_dispatcher_connect(
                self.hass,
                f"{SIGNAL_UPDATE}_{self._name}",
                self._handle_update,
            )
        )

    @callback
    def _handle_update(self, data):
        """Handle updated data from event."""
        self._update_data(data)
        self.async_write_ha_state()
