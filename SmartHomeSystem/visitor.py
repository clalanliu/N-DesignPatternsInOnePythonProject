# VisitorPattern.py
import logging
from abc import ABC, abstractmethod

from SmartHomeSystem import SmartDevice, SmartLight, SmartThermostat

logger = logging.getLogger(__name__)


class DeviceVisitor(ABC):
    def visit(self, device: SmartDevice):
        logger.info(f"Visitor {id(self)} visiting device {id(device)}")
        if isinstance(device, SmartThermostat):
            self.visit_smart_thermostat(device)
        if isinstance(device, SmartLight):
            self.visit_smart_light(device)

    @abstractmethod
    def visit_smart_light(self, smart_light):
        pass

    @abstractmethod
    def visit_smart_thermostat(self, smart_thermostat):
        pass


class DeviceStatusVisitor(DeviceVisitor):
    def visit_smart_light(self, smart_light):
        logger.info("Checking status of Smart Light.")
        smart_light.operate()

    def visit_smart_thermostat(self, smart_thermostat):
        logger.info("Checking status of Smart Thermostat.")
        smart_thermostat.operate()
