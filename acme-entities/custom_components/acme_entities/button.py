"""Button platform for ACME Entities."""
from homeassistant.components.button import ButtonEntity
from homeassistant.core import callback

from .const import DOMAIN, EVENT_STATUS, EVENT_RENEW

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the button platform."""
    known_certs = set()

    @callback
    def handle_event(event):
        cert_name = event.data.get("name")
        if not cert_name:
            return
        
        if cert_name not in known_certs:
            known_certs.add(cert_name)
            async_add_entities([AcmeRenewButton(hass, cert_name)])

    hass.bus.async_listen(EVENT_STATUS, handle_event)

class AcmeRenewButton(ButtonEntity):
    """Representation of an ACME Renew Button."""

    def __init__(self, hass, name):
        self.hass = hass
        self._cert_name = name
        self._attr_name = f"Renew ACME Certificate - {name}"
        self._attr_unique_id = f"acme_cert_renew_{name.replace('.', '_').replace('*', 'wildcard')}"
        self._attr_icon = "mdi:refresh"

    async def async_press(self) -> None:
        """Handle the button press."""
        self.hass.bus.async_fire(EVENT_RENEW, {"name": self._cert_name})
