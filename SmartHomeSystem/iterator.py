import logging
from typing import List

from SmartHomeSystem import SmartDevice

logger = logging.getLogger(__name__)


class DeviceIterator:
    def __init__(self, devices: List[SmartDevice]):
        self.devices = devices
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.devices):
            device = self.devices[self.index]
            self.index += 1
            return device
        else:
            raise StopIteration
