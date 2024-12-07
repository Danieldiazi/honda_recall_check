from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Configura la integración Honda Recall Check desde una entrada de configuración."""
    hass.data.setdefault(DOMAIN, {})

    # Almacena la configuración de la entrada para referencia
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Configurar las plataformas (sensor) de forma asíncrona
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Desinstala una entrada de configuración."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, ["sensor"])
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok





