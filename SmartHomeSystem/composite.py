import logging

from SmartHomeSystem import SmartDevice

logger = logging.getLogger(__name__)


class SmartDeviceGroup(SmartDevice):
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device):
        self.devices.remove(device)

    def operate(self):
        logger.info(f"Operating the SmartDeviceGroup {id(self)}.")
        for device in self.devices:
            device.operate()
