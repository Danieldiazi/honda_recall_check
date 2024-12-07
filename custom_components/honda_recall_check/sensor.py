from homeassistant.components.sensor import SensorEntity
from .honda_api import HondaRecallAPI
from .const import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Configura el sensor basado en config entry."""
    vin = config_entry.data["vin"]
    api = HondaRecallAPI(vin)

    async_add_entities([
        HondaRecallSensor(hass, vin, api),
        HondaRecallBooleanSensor(hass, vin, api)
    ])

class HondaRecallSensor(SensorEntity):
    """Sensor que devuelve el número de recalls."""

    def __init__(self, hass, vin, api):
        self.hass = hass
        self._vin = vin
        self._state = None
        self._recalls = []
        self._api = api

    @property
    def unique_id(self):
        return f"honda_recall_count_{self._vin.lower()}"

    @property
    def name(self):
        return f"Honda Recall Count ({self._vin})"

    @property
    def state(self):
        return len(self._recalls)

    @property
    def extra_state_attributes(self):
        return {"recalls": self._recalls}

    async def async_update(self):
        try:
            self._recalls = await self.hass.async_add_executor_job(self._api.check_recall)
        except Exception as e:
            self._recalls = []

class HondaRecallBooleanSensor(SensorEntity):
    """Sensor que devuelve True/False si hay recalls."""

    def __init__(self, hass, vin, api):
        self.hass = hass
        self._vin = vin
        self._state = False
        self._api = api

    @property
    def unique_id(self):
        return f"honda_recall_status_{self._vin.lower()}"

    @property
    def name(self):
        return f"Honda Recall Status ({self._vin})"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        try:
            recalls = await self.hass.async_add_executor_job(self._api.check_recall)
            self._state = len(recalls) > 0
        except Exception as e:
            self._state = False
