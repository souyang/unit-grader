from ..config.data import UNITS, HELP_INSTRUCTION
import typer
import numpy as np  # Import numpy for rounding
import traceback
import math


def is_valid_numeric_string(s):
    """
    Check if a string is a valid numeric string.
    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a valid numeric string, False otherwise.
    """
    try:
        float(s)  # Try to convert the string to a float
        return True  # If successful, it's a valid numeric string
    except ValueError:
        return False  # If it raises a ValueError, it's not a valid numeric string


def convert_units(input_value, from_unit, to_unit, category, conversion_data):
    """
    Convert an input value from one unit to another.

    Args:
        input_value (float): The input value to be converted.
        from_unit (str): The unit to convert from.
        to_unit (str): The unit to convert to.
        category (str): The category of the units (e.g., 'temperature' or 'volume').
        conversion_data (dict): The conversion data.

    Returns:
        float: The converted value.
        None: If the conversion cannot be performed.
    """
    # Perform the conversion
    try:
        # Validate the input parameters
        if category not in UNITS:
            raise ValueError(f"category {category} is not a valid category.")

        if (from_unit not in UNITS[category]) or (to_unit not in UNITS[category]):
            raise ValueError(
                f"from_unit {from_unit} is not a valid unit or to_unit {to_unit} is not a valid unit."
            )

        # if from_unit == to_unit return the output
        if from_unit == to_unit:
            return np.round(input_value, 1)

        # Define conversion factors for temperatures and volumes
        if (from_unit, to_unit) not in conversion_data[category]:
            raise ValueError(
                f"Conversion factor for {from_unit} to {to_unit} does not exist."
            )

        conversion_func = conversion_data[category][(from_unit, to_unit)]
        print(conversion_func)
        if not callable(conversion_func):
            raise ValueError(
                f"Conversion function {conversion_func} for {from_unit} to {to_unit} is not callable."
            )
        # Perform the conversion and avoid the floating point precision issue using numpy for rounding
        # checkout https://docs.python.org/3/library/functions.html#round for rounding issue in python3
        # checkout https://docs.python.org/3/tutorial/floatingpoint.html for precision issue
        converted_value = np.round((conversion_func(input_value)), 3)
        return np.round(converted_value, 1)
    except ValueError as e:
        typer.echo(f"Value Error: {e}")
        return None
    except Exception as e:
        typer.echo(f"Unexpected error occured: {e}")
        return None  # Cannot convert for any reason
