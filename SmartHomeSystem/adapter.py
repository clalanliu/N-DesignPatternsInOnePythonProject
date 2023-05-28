import logging
from abc import ABC, abstractmethod

from SmartHomeSystem import SmartDevice, WiFi

logger = logging.getLogger(__name__)


class ThirdPartySmartDevice(ABC):
    """Third party devices don't have the same interface as our SmartDevice."""

    @abstractmethod
    def switch_on(self):
        pass

    @abstractmethod
    def switch_off(self):
        pass


class ThirdPartySmartLight(ThirdPartySmartDevice):
    def switch_on(self):
        logger.info("ThirdPartySmartLight is turned on.")

    def switch_off(self):
        logger.info("ThirdPartySmartLight is turned off.")


class SmartDeviceAdapter(SmartDevice):
    """This adapter wraps a third party device so it can be used in our system."""

    def __init__(self, third_party_device):
        super().__init__(communication=WiFi())
        self.third_party_device = third_party_device

    def operate(self):
        super().operate()
        self.third_party_device.switch_on()
        self.third_party_device.switch_off()
