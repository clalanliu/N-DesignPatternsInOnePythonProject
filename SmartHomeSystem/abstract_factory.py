import logging
from abc import ABC, abstractmethod

from SmartHomeSystem import SmartLight, SmartThermostat
from SmartHomeSystem import Bluetooth, WiFi

logger = logging.getLogger(__name__)


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
