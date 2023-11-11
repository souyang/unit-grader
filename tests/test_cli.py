"""
    ------------------------------------------------
    This module contains the tests for the CLI app.
    ------------------------------------------------
    The following functions are tested:
        * grade_conversion
        * get_project_meta
        * version_callback
        * enable_verbose

"""
import pytest
import pytest_mock
from typer import Exit
from typer.testing import CliRunner

from unit_grader.cli import (
    app,
    app_name,
    get_project_meta,
    version_callback,
    enableLogging,
)
from unit_grader.config.data import UNEXPECTED_EXIT
from unit_grader.config.enums import Answer
import logging

LOGGER = logging.getLogger(__name__)
# Create a CliRunner for testing the CLI app
runner = CliRunner()

grad_response_function_name = "unit_grader.commands.conversion_grader.grade_response"
get_project_meta_function_name = "unit_grader.cli.get_project_meta"


# Test the grade_conversion CLI command
def test_grade_conversion_without_verbose(mocker: pytest_mock.MockFixture) -> None:
    """
    Test the grade_conversion CLI command
      with correct arugments but without verbose mode

    Expected Behavior:
    -------------------
    Ensure that correct answer is returned
      and verbose messages are not printed.
    """
    mocker.patch(
        grad_response_function_name,
        return_value=Answer.CORRECT,
    )
    result = runner.invoke(
        app,
        [
            "--input-value",
            "32",
            "--from-unit",
            "Celsius",
            "--to-unit",
            "Kelvin",
            "--student-response",
            "305.2",
        ],
    )
    assert "Verbose mode is enabled." not in result.output
    assert "input_value: 32" not in result.output
    assert "from_unit: Celsius" not in result.output
    assert "to_unit: Kelvin" not in result.output
    assert "student_response: 305.2" not in result.output
    assert result.exit_code == 0
    assert Answer.CORRECT.value in result.output


@pytest.fixture
def setup_logging():
    logging.basicConfig(level=logging.NOTSET)


def test_enable_verbose(
    capfd: pytest.CaptureFixture, mocker: pytest_mock.MockerFixture
) -> None:
    """
    Test the enable_verbose function
     when verbose is True

    Expected Behavior:
    -------------------
    Ensure that verbose mode is enabled
    """
    mock_logger_basicConfig = mocker.patch("logging.basicConfig")
    enableLogging(verbose=True)
    mock_logger_basicConfig.assert_called_once_with(
        level=logging.DEBUG, format="[%(levelname)s] %(message)s"
    )
    captured = capfd.readouterr()
    assert "Verbose mode is enabled." in captured.out


def test_enableLogging_non_verbose(
    capfd: pytest.CaptureFixture, mocker: pytest_mock.MockerFixture
) -> None:
    mock_logger_basicConfig = mocker.patch("logging.basicConfig")
    enableLogging(verbose=False)
    mock_logger_basicConfig.assert_called_once_with(
        level=logging.INFO, format="[%(levelname)s] %(message)s"
    )
    captured = capfd.readouterr()
    assert "Verbose mode is enabled." not in captured.out


def test_grade_conversion_verbose(
    mocker: pytest_mock.MockFixture, caplog: pytest.CaptureFixture
) -> None:
    """
    Test the grade_conversion CLI command with correct arugments and verbose mode

    Expected Behavior:
    -------------------
    Ensure that correct answer is returned and verbose messages are printed.

    """
    mocker.patch(
        grad_response_function_name,
        return_value=Answer.CORRECT,
    )
    caplog.set_level(logging.DEBUG)
    result = runner.invoke(
        app,
        [
            "--input-value",
            "32",
            "--from-unit",
            "Celsius",
            "--to-unit",
            "Kelvin",
            "--student-response",
            "305.2",
            "--verbose",
        ],
    )
    assert result.exit_code == 0
    assert "Verbose mode is enabled." in result.output
    assert "input_value: 32" in caplog.text
    assert "from_unit: Celsius" in caplog.text
    assert "to_unit: Kelvin" in caplog.text
    assert "student_response: 305.2" in caplog.text
    assert Answer.CORRECT.value in result.output


def test_get_project_meta(mocker: pytest_mock.MockFixture) -> None:
    """
    Test the get_project_meta function
     when correct data is present in pyproject.toml.

    Expected Behavior:
    -------------------
    Ensure that the function returns json content.

    """
    # Define a sample TOML content loaded from pyproject.toml
    sample_toml_content = b"""
    [project]
    name = "my_project"
    version = "1.0.0"
    """

    # Create a mocker fixture to mock the open function
    mocker.patch("builtins.open", mocker.mock_open(read_data=sample_toml_content))

    # Create a mock for 'tomli.load' function
    mocker.patch(
        "tomli.load",
        return_value={"project": {"name": "my_project", "version": "1.0.0"}},
    )

    project_meta = get_project_meta()

    # Assert that the 'tomli.load' function was called with the correct data
    assert project_meta == {"name": "my_project", "version": "1.0.0"}


def test_not_get_project_meta_valid_toml(mocker: pytest_mock.MockFixture) -> None:
    """
    Test the get_project_meta function
     when incorrect data is present in pyproject.toml.

    Expected Behavior:
    -------------------
    Ensure that the function returns None.

    """
    # Define a sample TOML content loaded from pyproject.toml
    sample_toml_content = b"""
    [test]
    name = "my_project"
    version = "1.0.0"
    """

    # Create a mocker fixture to mock the open function
    mocker.patch("builtins.open", mocker.mock_open(read_data=sample_toml_content))

    # Create a mock for 'tomli.load' function
    mocker.patch(
        "tomli.load",
        return_value={"test": {"name": "my_project", "version": "1.0.0"}},
    )

    project_meta = get_project_meta()

    # Assert that the 'tomli.load' function was called with wrong data
    assert project_meta is None


def test_not_get_project_meta_invalid_toml(mocker: pytest_mock.MockFixture) -> None:
    """
    Test the get_project_meta function
     when incorrect data is present in pyproject.toml.

    Expected Behavior:
    -------------------
    Ensure that the function returns None.

    """
    # Define a sample TOML content loaded from pyproject.toml
    sample_toml_content = b"""
    test
    name = "my_project"
    version = "1.0.0"
    """

    # Create a mocker fixture to mock the open function
    mocker.patch("builtins.open", mocker.mock_open(read_data=sample_toml_content))

    project_meta = get_project_meta()

    # Assert that the 'tomli.load' function was called with wrong data
    assert project_meta is None


def test_version_callback(
    mocker: pytest_mock.MockerFixture, capsys: pytest_mock.MockerFixture
) -> None:
    mocker.patch(
        get_project_meta_function_name,
        return_value={"version": "1.0.0", "name": app_name},
    )  # Mock get_project_meta function
    """
    Test the version_callback function
     when correct version data is present in pyproject.toml.

    Expected Behavior:
    -------------------
    Ensure that the function returns version information.

    """
    with pytest.raises(Exit):
        version_callback(True)  # Call the function
    # Capture the output using capsys
    captured = capsys.readouterr()
    output = captured.out.strip()
    assert output == f"{app_name}: 1.0.0"


def test_version_callback_no_version_data(
    mocker: pytest_mock.MockerFixture, capsys: pytest_mock.MockerFixture
) -> None:
    """
    Test the version_callback function
     when no version data is present in pyproject.toml.

    Expected Behavior:
    -------------------
    Ensure that the function's output contains "Unable to get version information."

    """
    mocker.patch(
        get_project_meta_function_name, return_value={"test": "1.0.0"}
    )  # Mock get_project_meta function
    with pytest.raises(Exit):
        version_callback(True)  # Call the function
    # Capture the output using capsys
    captured = capsys.readouterr()
    output = captured.out.strip()
    assert (
        output
        == f"[bold red]Unable to get version information. {UNEXPECTED_EXIT}[/bold red]"
    )
