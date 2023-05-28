import copy
import logging

logger = logging.getLogger(__name__)


class SmartDevicePrototype:
    def clone(self):
        return copy.deepcopy(self)
