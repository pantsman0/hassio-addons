"""The ACME Entities Companion integration."""
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, EVENT_RENEW, SERVICE_RENEW

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the ACME Entities integration."""
    _LOGGER.info("Setting up ACME Entities Companion Integration")
    hass.data.setdefault(DOMAIN, {})

    hass.async_create_task(
        hass.helpers.discovery.async_load_platform("sensor", DOMAIN, {}, config)
    )
    hass.async_create_task(
        hass.helpers.discovery.async_load_platform("button", DOMAIN, {}, config)
    )

    async def handle_renew(call):
        """Handle the renew service call."""
        cert_name = call.data.get("cert_name")
        if cert_name:
            hass.bus.async_fire(EVENT_RENEW, {"name": cert_name})

    hass.services.async_register(DOMAIN, SERVICE_RENEW, handle_renew)
    return True
