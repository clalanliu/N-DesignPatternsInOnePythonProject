import logging
from abc import ABC, abstractmethod

from SmartHomeSystem import (
    Bluetooth,
    WiFi,
    SmartDevice,
    CommunicationTechnology,
    TemperatureControlStrategy,
)

logger = logging.getLogger(__name__)


class SmartLight(SmartDevice):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def operate(self):
        super().operate()
        self.turn_on()
        self.turn_off()


class SmartThermostat(SmartDevice):
    @abstractmethod
    def increase_temperature(self):
        pass

    @abstractmethod
    def decrease_temperature(self):
        pass

    def __init__(self, communication: CommunicationTechnology):
        super().__init__(communication)
        self.control_strategy: TemperatureControlStrategy = None

    def operate(self):
        super().operate()
        self.increase_temperature()
        self.decrease_temperature()

    def set_temperature_control_strategy(
        self, control_strategy: TemperatureControlStrategy
    ):
        self.control_strategy = control_strategy(
            increase_func=self.increase_temperature,
            decrease_func=self.decrease_temperature,
        )

    def control_temperature(self):
        if self.control_strategy:
            self.control_strategy.control_temperature()


class LivingRoomSmartLight(SmartLight):
    def turn_on(self):
        logger.info("Living Room's Smart Light is turned on.")

    def turn_off(self):
        logger.info("Living Room's Smart Light is turned off.")


class KitchenRoomSmartLight(SmartLight):
    def turn_on(self):
        logger.info("Kitchen Room's Smart Light is turned on.")

    def turn_off(self):
        logger.info("Kitchen Room's Smart Light is turned off.")


class LivingRoomSmartThermostat(SmartThermostat):
    def increase_temperature(self):
        logger.info("Living Room's Smart Thermostat is increasing temperature.")

    def decrease_temperature(self):
        logger.info("Living Room's Smart Thermostat is decreasing temperature.")

    def set_temperature(self, temp):
        logger.info(f"Living Room's Smart Thermostat is set to {temp}")


class KitchenRoomSmartThermostat(SmartThermostat):
    def increase_temperature(self):
        logger.info("Kitchen Room's Smart Thermostat is increasing temperature.")

    def decrease_temperature(self):
        logger.info("Kitchen Room's Smart Thermostat is decreasing temperature.")


class SmartDeviceFactory(ABC):
    @abstractmethod
    def create_smart_light(self):
        pass

    @abstractmethod
    def create_smart_thermostat(self):
        pass


class LivingRoomDeviceFactory(SmartDeviceFactory):
    def create_smart_light(self):
        return LivingRoomSmartLight(WiFi())

    def create_smart_thermostat(self):
        return LivingRoomSmartThermostat(Bluetooth())


class KitchenRoomDeviceFactory(SmartDeviceFactory):
    def create_smart_light(self):
        return KitchenRoomSmartLight(WiFi())

    def create_smart_thermostat(self):
        return KitchenRoomSmartThermostat(Bluetooth())
