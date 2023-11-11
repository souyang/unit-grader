"""
This module provides a CLI tool for converting units of
measure and grading student responses to conversion questions.

Main Functions:
    - grade_response: Grade a student's response to a conversion question.
    - Allow users to specify parameters via CLI arguments such as:
        - input_value: The input value provided in the question.
        - from_unit: The unit mentioned in the question.
        - to_unit: The target unit mentioned in the question.
        - student_response: The student's response.
"""
import logging
import os
from typing import Optional

import tomli
import typer
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn

from unit_grader.commands.conversion_grader import grade_response
from unit_grader.config.data import UNEXPECTED_EXIT, UNIT_CONVERSION_INSTRUCTIONS

app = typer.Typer()  # creates a CLI app
app_name = "unit-grader"


def get_project_meta() -> Optional[dict[str, str]]:
    """
    Get the project metadata from the pyproject.toml file.

    Args:
        None

    Returns:
        dict: The project metadata.
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        version_file_path = os.path.join(script_dir, "../../pyproject.toml")
        with open(version_file_path, mode="rb") as pyproject:
            return tomli.load(pyproject)["project"]
    except (IOError, KeyError):
        return None  # Handle file I/O errors or missing 'project' key


def version_callback(show_version: bool) -> None:
    """
    Get the project version from the pyproject.toml file.

    Args:
        show_version (bool): A flag to indicate whether to show the version.

    Returns:
        None
    """

    if show_version:
        pkg_meta = get_project_meta()
        if "version" not in pkg_meta:
            typer.echo(f"Unable to get version information. {UNEXPECTED_EXIT}")
        else:
            app_version = str(pkg_meta["version"])
            typer.echo(f"{app_name}: {app_version}")
        raise typer.Exit()


def enableLogging(verbose: bool) -> None:
    lvl = logging.INFO
    fmt = "[%(levelname)s] %(message)s"
    if verbose:
        print("[green]Verbose mode is enabled.[/green]")
        lvl = logging.DEBUG
    logging.basicConfig(level=lvl, format=fmt)


@app.command(name=app_name, no_args_is_help=True)
def grade_conversion(
    input_value: str = typer.Option(
        ..., "--input-value", "-i", help="Input numerical value."
    ),
    from_unit: str = typer.Option(
        ...,
        "--from-unit",
        "-f",
        help=f"Input conversion unit: {UNIT_CONVERSION_INSTRUCTIONS}",
    ),
    to_unit: str = typer.Option(
        ...,
        "--to-unit",
        "-t",
        help=f"Target conversion unit: {UNIT_CONVERSION_INSTRUCTIONS}",
    ),
    student_response: str = typer.Option(
        ..., "--student-response", "-s", help="Student's response."
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output."
    ),
    version: bool = typer.Option(
        False, "--version", "-V", callback=version_callback, is_eager=True
    ),
) -> None:
    """

    Unit Conversion Grader Tool to grade a student's
    response to the unit conversion question.

    Student's response must match the correct answer after both value are
    rounded to the tenths place.

    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        conversion_task = progress.add_task(description="Processing...", total=1)
        enableLogging(verbose)
        logging.debug(f"input_value: {input_value}")
        logging.debug(f"from_unit: {from_unit}")
        logging.debug(f"to_unit: {to_unit}")
        logging.debug(f"student_response: {student_response}")
        result = grade_response(input_value, from_unit, to_unit, student_response)
        progress.update(conversion_task, completed=1)
        progress.stop()
        print(f"[yellow bold]{result.value}[/yellow bold]")


if __name__ == "__main__":
    app()
