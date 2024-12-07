import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

CONFIG_SCHEMA = vol.Schema({
    vol.Required("vin"): str,
    vol.Optional("scan_interval", default=60): int,  # Intervalo predeterminado: 60 minutos
})

class HondaRecallConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gestiona el flujo de configuración de Honda Recall Check."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Primer paso del flujo de configuración."""
        errors = {}
        if user_input is not None:
            if len(user_input["vin"]) < 5:
                errors["base"] = "vin_invalid"
            else:
                return self.async_create_entry(
                    title=f"Honda VIN {user_input['vin']}",
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=CONFIG_SCHEMA,
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Permite gestionar opciones desde la UI."""
        return HondaRecallOptionsFlowHandler(config_entry)

class HondaRecallOptionsFlowHandler(config_entries.OptionsFlow):
    """Maneja las opciones desde la interfaz."""

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Paso inicial para editar opciones."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required("scan_interval", default=self.config_entry.options.get("scan_interval", 60)): int,
            }),
        )
