import logging
from abc import ABC, abstractmethod

from SmartHomeSystem import SmartLight, SmartThermostat

logger = logging.getLogger(__name__)


class SmartHomeFacade:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def turn_all_lights_on_and_off(self):
        logger.info(f"Facade {id(self)} is operating devices")
        for device in self.devices:
            if isinstance(device, SmartLight):
                device.operate()

    def adjust_temperature(self, temperature):
        logger.info(f"Facade {id(self)} is operating devices")
        for device in self.devices:
            if isinstance(device, SmartThermostat):
                if temperature > 25:
                    device.increase_temperature()
                else:
                    device.decrease_temperature()
