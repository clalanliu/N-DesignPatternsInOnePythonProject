import logging
from dataclasses import dataclass

from SmartHomeSystem import SmartThermostat, SmartLight

logger = logging.getLogger(__name__)


class Expression:
    def interpret(self, context):
        pass


class LightOnExpression(Expression):
    def __init__(self, light):
        self.light = light

    def interpret(self, context):
        if context == "ON":
            self.light.turn_on()
        else:
            logger.info("Invalid context for LightOnExpression.")


class LightOffExpression(Expression):
    def __init__(self, light):
        self.light = light

    def interpret(self, context):
        if context == "OFF":
            self.light.turn_off()
        else:
            logger.info("Invalid context for LightOffExpression.")


class ThermostatSetExpression(Expression):
    def __init__(self, thermostat: SmartThermostat, temperature: float):
        self.thermostat = thermostat
        self.temperature = temperature

    def interpret(self, context):
        if context.isdigit():
            self.thermostat.set_temperature(int(context))
        else:
            logger.info("Invalid context for ThermostatSetExpression.")
