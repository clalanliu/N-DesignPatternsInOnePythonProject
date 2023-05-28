import logging
from abc import ABC, abstractmethod

from SmartHomeSystem import SmartDevice

logger = logging.getLogger(__name__)


class SmartDeviceDecorator(SmartDevice):
    def __init__(self, device):
        self.device = device

    def operate(self):
        self.device.operate()


class MotionSensor(SmartDeviceDecorator):
    def operate(self):
        super().operate()
        self.detect_motion()

    def detect_motion(self):
        logger.info("Motion detected!")


class VoiceControl(SmartDeviceDecorator):
    def operate(self):
        super().operate()
        self.activate_voice_control()

    def activate_voice_control(self):
        logger.info("Voice control activated!")
