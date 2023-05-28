import logging

from SmartHomeSystem import SmartDevice

logger = logging.getLogger(__name__)


class SmartDeviceProxy(SmartDevice):
    def __init__(self, device: SmartDevice):
        self.device = device

    def operate(self):
        self._check_access()
        self.device.operate()

    def _check_access(self):
        logger.info("Access control check passed.")
