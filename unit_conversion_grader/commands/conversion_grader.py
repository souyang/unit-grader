from ..config.enums import Answer
from ..config.data import UNITS, HELP_INSTRUCTION, CONVERSION_DATA
from ..utils.common import convert_units, is_valid_numeric_string
import typer
import numpy as np  # Import numpy for rounding


def check_unit_existence(dictionary, unit_to_check):
    """
    Check if a unit exists in a dictionary.
    Args:
        dictionary (dict): The dictionary to check.
        unit_to_check (str): The unit to check.
    Returns:
        str: The category of the unit (e.g., 'temperature' or 'volume').
        None: If the unit does not exist.
    """
    for key, units in dictionary.items():
        print(unit_to_check)
        print(units)
        if unit_to_check in units:
            return key
    return None


def validate_input(from_unit, to_unit, input_value):
    """
    Validate the input values
    Args:
        from_unit (str): The unit to convert from.
        to_unit (str): The unit to convert to.
        input_value (str): The input value to be converted.
    Returns:
        str: The category of the units (e.g., 'temperature' or 'volume').
        None: If the input is invalid.
    """
    try:
        from_unit_category = check_unit_existence(UNITS, from_unit)
        to_unit_category = check_unit_existence(UNITS, to_unit)

        if from_unit_category is None:
            raise ValueError(f"{from_unit} is the invalid unit. {HELP_INSTRUCTION}")

        if to_unit_category is None:
            raise ValueError(f"{to_unit} is the invalid unit. {HELP_INSTRUCTION}")

        if from_unit_category != to_unit_category:
            raise ValueError(
                f"{from_unit}'s unit category is {from_unit_category} and {to_unit}'s unit category is {to_unit_category}. {HELP_INSTRUCTION}"
            )

        if not is_valid_numeric_string(input_value):
            raise ValueError(
                f"{input_value} as input_value needs to be numeric. {HELP_INSTRUCTION}"
            )
    except ValueError as e:
        typer.echo(f"Value Error: {e}")
        return None
    except Exception as e:
        typer.echo(f"Unexpected exception: {e}")
        return None
    return from_unit_category


def grade_response(input_value, from_unit, to_unit, student_response):
    """
    Grade a student's response to a conversion question.

    Args:
        input_value (str): The input value provided in the question.
        from_unit (str): The unit mentioned in the question.
        to_unit (str): The target unit mentioned in the question.
        student_response (str): The student's response.

    Returns:
        Answer: The result of the grading, one of [Answer.CORRECT, Answer.INCORRECT, Answer.INVALID].
    """
    # unit name validation
    category = validate_input(from_unit, to_unit, input_value)

    if category is None:  # invalid input
        return Answer.INVALID

    if not is_valid_numeric_string(student_response):
        return Answer.INCORRECT

    if from_unit == to_unit:
        if np.round(float(input_value), 1) == np.round(float(student_response), 1):
            return Answer.CORRECT
        else:
            return Answer.INCORRECT

    student_response = np.round(float(student_response), 1)
    input_numeric_value = float(input_value)
    convert_value = convert_units(
        input_numeric_value, from_unit, to_unit, category, CONVERSION_DATA
    )
    if convert_value is None:
        return Answer.INVALID
    elif convert_value == student_response:
        return Answer.CORRECT
    else:
        return Answer.INCORRECT
