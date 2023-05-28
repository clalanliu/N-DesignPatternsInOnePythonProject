import logging
from abc import ABC, abstractmethod
from SmartHomeSystem import Room

from SmartHomeSystem import SmartThermostat

logger = logging.getLogger(__name__)


class Observer(ABC):
    @abstractmethod
    def update(self, sender, event):
        pass


class AlertSystem(Observer):
    def update(self, sender: Room, event: str):
        logger.info(f"Alert! Room {id(sender)} reports a {event}!")
