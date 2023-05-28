import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class TemperatureControlStrategy(ABC):
    def __init__(self, increase_func, decrease_func) -> None:
        self.increase_func = increase_func
        self.decrease_func = decrease_func

    @abstractmethod
    def control_temperature(self):
        pass


class NormalTemperatureControl(TemperatureControlStrategy):
    def control_temperature(self):
        logger.info("Applying normal temperature control.")


class EcoTemperatureControl(TemperatureControlStrategy):
    def control_temperature(self):
        logger.info("Applying eco temperature control.")
