"""
    This module provides a CLI tool for converting units of measure and grading student responses to conversion questions. 

    Main Functions:
    - grade_response: Grade a student's response to a conversion question.
    - Allow users to specify parameters via CLI arguments such as:
        - input_value: The input value provided in the question.
        - from_unit: The unit mentioned in the question.
        - to_unit: The target unit mentioned in the question.
        - student_response: The student's response.
"""
import typer

from unit_conversion_grader.commands.conversion_grader import grade_response

app = typer.Typer()  # creates a CLI app


@app.command()
def grade_conversion(
    input_value: str = typer.Option(
        ..., "--input-value", "-i", help="Input numerical value"
    ),
    from_unit: str = typer.Option(
        ...,
        "--from-unit",
        "-f",
        help="Input unit of measure: Kelvin, Celsius, Fahrenheit,Rankine, liters, tablespoons, cubic-inches, cups, cubic-feet, gallons",
    ),
    to_unit: str = typer.Option(
        ...,
        "--to-unit",
        "-t",
        help="Target unit of measure: Kelvin, Celsius, Fahrenheit,Rankine, liters, tablespoons, cubic-inches, cups, cubic-feet, gallons",
    ),
    student_response: str = typer.Option(
        ..., "--student-response", "-s", help="Student's response"
    ),
):
    """
    Grade a student's response to a conversion question.
    """
    result = grade_response(input_value, from_unit, to_unit, student_response)
    typer.echo(f"Result: {result.value}")


if __name__ == "__main__":
    app()
