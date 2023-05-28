import copy
import logging

logger = logging.getLogger(__name__)


class SmartDevicePrototype:
    def clone(self):
        return copy.deepcopy(self)


class ConfiguredSmartLight(SmartDevicePrototype):
    def __init__(self, brightness, color):
        self.brightness = brightness
        self.color = color


if __name__ == "__main__":
    original_light = ConfiguredSmartLight(75, "Blue")
    cloned_light = original_light.clone()
    logger.info(
        f"Cloned light configuration: brightness = {cloned_light.brightness}, color = {cloned_light.color}"
    )
