import logging
from abc import ABC, abstractmethod

from SmartHomeSystem import SmartDevicePrototype

logger = logging.getLogger(__name__)


class CommunicationTechnology(ABC):
    """Implementor interface for communication technology."""

    @abstractmethod
    def communicate(self):
        pass


class Bluetooth(CommunicationTechnology):
    def communicate(self):
        logger.info("Communicating via Bluetooth.")


class WiFi(CommunicationTechnology):
    def communicate(self):
        logger.info("Communicating via Wi-Fi.")


# Base SmartDevice class
# Update SmartDevice and its children
class SmartDevice(ABC, SmartDevicePrototype):
    def __init__(self, communication):
        self.observers = []
        self.communication = communication

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(self, event)

    def operate(self):
        self.notify(
            f"event from device {id(self)}"
        )  # Notify observers when device is operated
        self.communication.communicate()

    def accept(self, visitor):
        visitor.visit(self)
