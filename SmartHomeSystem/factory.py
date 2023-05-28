import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class AlertCreator(ABC):
    @abstractmethod
    def create_alert(self):
        pass


class Alert(ABC):
    @abstractmethod
    def send(self):
        pass


class FireAlert(Alert):
    def send(self):
        logger.info("Fire Alert: Smoke detected in the house!")


class IntruderAlert(Alert):
    def send(self):
        logger.info("Intruder Alert: Motion detected in the house!")


class FireAlertCreator(AlertCreator):
    def create_alert(self):
        return FireAlert()


class IntruderAlertCreator(AlertCreator):
    def create_alert(self):
        return IntruderAlert()
