import logging
from abc import ABC, abstractmethod

from SmartHomeSystem import SmartLight

logger = logging.getLogger(__name__)


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class TurnOnCommand(Command):
    def __init__(self, light: SmartLight):
        self.light = light

    def execute(self):
        self.light.turn_on()


class TurnOffCommand(Command):
    def __init__(self, light: SmartLight):
        self.light = light

    def execute(self):
        self.light.turn_off()


class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
