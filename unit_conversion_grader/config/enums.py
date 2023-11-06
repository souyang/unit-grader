"""
This module contains the enums used in the conversion data.
"""
from enum import Enum


class Answer(Enum):
    CORRECT = "correct"
    INCORRECT = "incorrect"
    INVALID = "invalid"


class UnitCategory(Enum):
    TEMPERATURE = "temperature"
    VOLUME = "volume"


class TemperatureUnits(Enum):
    KELVIN = "Kelvin"
    CELSIUS = "Celsius"
    FAHRENHEIT = "Fahrenheit"
    RANKINE = "Rankine"


class VolumeUnits(Enum):
    LITERS = "liters"
    TABLESPOONS = "tablespoons"
    CUBIC_INCHES = "cubic-inches"
    CUPS = "cups"
    CUBIC_FEET = "cubic-feet"
    GALLONS = "gallons"
