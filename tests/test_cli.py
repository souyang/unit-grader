# tests/test_main.py

import typer
from typer.testing import CliRunner
import pytest
from pytest_mock import mocker
from unit_conversion_grader.cli import app, grade_conversion
from unit_conversion_grader.commands.conversion_grader import grade_response, Answer

# Create a CliRunner for testing the CLI app
runner = CliRunner()

# Mock the grade_response function to simulate its behavior
@pytest.fixture
def mock_grade_response(mocker):
    mocker.patch(
        "unit_conversion_grader.commands.conversion_grader.grade_response",
        return_value=Answer.CORRECT,
    )

# Test the grade_response function
def test_grade_response():
    result = grade_response('32', 'Celsius', 'Kelvin', '305.2')
    assert result == Answer.CORRECT

# Test the grade_conversion CLI command
def test_grade_conversion(mock_grade_response):
    result = runner.invoke(app, [
        "--input-value", "32",
        "--from-unit", "Celsius",
        "--to-unit", "Kelvin",
        "--student-response", "305.2"
    ])
    assert result.exit_code == 0
    #assert "Result: CORRECT" in result.stdout
