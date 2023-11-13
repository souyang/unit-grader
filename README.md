# Unit Conversion Grader

## Overview
Unit Conversion Grader a command-line interface (CLI) program that allows you to convert among units of measurement and grade the users response to determine the result.

## Installation

Choose either **stable release** or **development**.

### Python and Pip Installation
Please ensure you download and install python3.9+ and pip. Checkout [python official website](https://www.python.org/downloads/) and [pip official website](https://pip.pypa.io/en/stable/cli/pip_download/) for detail.

### Stable Release

- `python -m pip install unit-grader`
- Test the CLI to verify the installation via running `unit-grader -i 100  -f Kelvin -t Celsius -s -173.15`

### Development
- Install Python with version 3.9 or higher
- Follow [official documentation](https://github.com/pdm-project/pdm#installation) to install PDM
- `git clone https://github.com/souyang/unit-grader.git`
- `cd unit-grader`
- `pdm install`
- `python3 -m pip install -e .`
- Test the CLI to verify the installation via running `unit-grader -i 100  -f Kelvin -t Celsius -s -173.15`

## Accomplished Tasks
- [x] Teacher provides `input-value`(input numeric value), `from-unit`(input unit of measnure), `to-unit` (a target unit of value), `student-response` (student's numeric response)
- [x] System indicates the response is `correct`, `incorrect` or `invalid`.
- [x] Stuent's response is correct if the response is equal to the answer after response and answer are rounded to tenths place.
- [x] Unit Testing Coverage is 100%. CI pipeline will fail if coverage is less than 100%.
- [x] `Sphinx` is used in pre-commit hook and CI/CD pipeline for generating api documentation.
- [x] A CI/CD pipeline is created. CI will be triggered when a pull request is created with target branch is `main` or a commit is merged to `main`. CD will be triggered after a commit is merged to `main`. 
- [x] The executable deployment is on [pypi](https://pypi.org/project/unit-grader/) and api documentation deployment is on [Netlify](https://unit-grader-api-docs.netlify.app/)
- [x] Versioning and Verbose are both implemented.
- [x] Pre-Commit hook is created to catch the problems early such as spelling, linting, formatting, docstring, configuration for best code quality in every commit.
- [x] Error reporting is provided to the end user when answer is invalid.
- [x] User feedback mechanism is setup for enhancing user requirements
- [x] Logging is enabled, user will see diagnose information when `--verbose` or `-v` as the option is set.
- [x] Colorized output for user distinguish between different types of information.
- [x] Progress Bar is enabled for long-running tasks.

## Future Tasks
- [ ] [Feature Flag Integration](FUTURE_WORK.md#feature-flag-integration)
- [ ] [Interactive Mode Option](FUTURE_WORK.md#interactive-mode-optoin)
- [ ] [Configuration Management](FUTURE_WORK.md#configuration-management)
- [ ] [Observeability](FUTURE_WORK.md#observeability)
- [ ] [Dockerization](FUTURE_WORK.md#dockerization)
- [ ] [Localization](FUTURE_WORK.md#localization)



## Third-Party Tools Overview

In the development of this project, we've leveraged the following third-party tools to enhance functionality and streamline development:

- [PDM](THIRD_PARTY_TOOLS.md#pdm): A Python project management tool and package installer.
- [Typer](THIRD_PARTY_TOOLS.md#typer): A Python library for building command-line applications.
- [Tomli](THIRD_PARTY_TOOLS.md#Tomli): A Python library for reading TOML and parse it to a json string.
- [Pre-Commit](THIRD_PARTY_TOOLS.md#pre-commit): A framework for managing and maintaining multi-language pre-commit hooks.
- [codespell](THIRD_PARTY_TOOLS.md#codespell): A tool designed to catch spelling mistakes in code.
- [Pytest](THIRD_PARTY_TOOLS.md#pytest): A testing framework for Python.
- [Ruff](THIRD_PARTY_TOOLS.md#ruff): A linter and formatter for Python.
- [Sphinx](THIRD_PARTY_TOOLS.md#sphinx): A documentation generator for Python projects.
- [bump-my-version](THIRD_PARTY_TOOLS.md#bump-my-version): A small command line tool to simplify releasing software by updating all version strings in code by the correct increment and optionally commit and tag the changes.

For detailed information about each tool and why we chose them, refer to the [detailed documentation](THIRD_PARTY_TOOLS.md).

## Command Usage

### Syntax
```bash
unit-grader -i <input-value> -f <from-unit> -t <to-unit> -s <student-response>
```

### General Instructions
- Provide `input-value`, `from-unit`, `to-unit`, `student-response` as input.
- `from-unit` and `to-unit` must be in the same unit meansurement category.
- Expected output: `correct`, `incorrect`, `invalid`.
- Supported unit meansurement categories include `temperature` and `volume`.
- units supported in `temperature` category: `Kelvin`, `Celsius`, `Fahrenheit` and `Rankine`. 
- units supported in `volume` category: `liters`, `tablespoons`, `cubic-inches`, `cups`, `cubic-feet`, `gallons`.
- Regarding volume units, `tablespoons` means `us tablespoons`, cubic-inches means `cups` means `us cups`, gallons means `us gallons`, 
- Name of each unit is case sensitive.
- Student's response must match the correct answer after both value are rounded to the tenths place.
- The rounding strategy follows round half to even (Banker's rounding). For example round(4.65, 1) == 4.6 and round(4.75, 1) == 4.8.

### Examples
```bash
unit-grader -i 50  -f Kelvin -t Celsius -s 30 # output: incorrect
unit-grader -i 100  -f Kelvin -t Celsius -s -173.15 # output: correct
unit-grader -i dog  -f Kelvin -t Celsius -s -173.15 # output: invalid

```

### Get Help
- Run `unit-grader --help` to get information

### Get Version
- Run `unit-grader --version` to get information

### Grade the student response based on inputs
- `unit-grader` has four required fields
  - `input-value (i)`: a numeric value
  - `from-unit (f)`: input unit of measure
  - `to-unit (t)`: target unit of measure
  - `student-response (s)` : student's numeric response

  Possible use cases:

| Sample Command | Input Value | Input Unit |  Target Unit| Student Response | Output
| ---------|----------|----------|----------|----------|----------|
| `unit-grader -i 50  -f Kelvin -t Celsius -s 30` | 50 | Kelvin | Celsius | 30 | incorrect
| `unit-grader -i 50  -f Kelvin -t Celsius -s dog` | 50 | Kelvin | Celsius | dog | incorrect
| `unit-grader -i 100  -f Kelvin -t Celsius -s -173.15` | 100 | Kelvin | Celsius | -173.15 | correct
| `unit-grader -i 100  -f cups -t liters -s 23.66` | 100 | cups | liters | 23.66 | correct
| `unit-grader -i dog  -f Kelvin -t Celsius -s -173.15` | dog | Kelvin | Celsius | 30 | invalid
| `unit-grader -i 100  -f Kelvin -t gallons -s -173.15` | 100 | Kelvin | gallons | 30 | invalid
| `unit-grader -i 100  -f dog -t gallons -s -173.15` | 100 | dog | gallons | 30 | invalid
| `unit-grader -i 100  -f Kelvin -t dog -s -173.15` | 100 | dog | gallons | 30 | invalid

## Advanced Usage

### Detail information in Verbose Mode 
You can get the detail information of your input in verbose mode for debugging purpose.
For example, `unit-grader -i 100  -f Kelvin -t dog -s -173.15 -v` will print out the messages

```
Verbose mode is enabled.
input-value: 100
from_unit: Celsius
to_unit: Kelvin
student_response: 305.2
```

## Error Handling
| Use Case | Sample Command | Expected Message Reported to user
| ---------|----------|----------|
| `Input numeric value` is not a number | `unit-grader -i dog  -f Kelvin -t Celsius -s -173.15` | Input Error: dog as input_value needs to be a number. Please use --help to see valid options.
| `Input unit of measure` is not supported or invalid | `unit-grader -i 100  -f Test -t Celsius -s -173.15` | Input Error: Test as from_unit is not supported. Select a conversion unit (Kelvin, Celsius,Fahrenheit,Rankine for temperature; liters, tablespoons, cubic-inches, cups, cubic-feet, gallons for volume). Please note that the unit is case-sensitive.
| `Target unit of measure` is not supported or invalid | `unit-grader -i 100  -f Test -t Celsius -s -173.15` | Input Error: Test as from_unit is not supported. Select a conversion unit (Kelvin, Celsius,Fahrenheit,Rankine for temperature; liters, tablespoons, cubic-inches, cups, cubic-feet, gallons for volume). Please note that the unit is case-sensitive.
| `Input unit of measure` and `Target unit of measure` are not in the same category | `unit-grader -i 100  -f cups -t Celsius -s -173.15` | Input Error: Ensure the selected conversion units match their respective categories for a valid conversion. Select a conversion unit (Kelvin, Celsius,Fahrenheit,Rankine for temperature; liters, tablespoons, cubic-inches, cups, cubic-feet, gallons for volume). Please note that the unit is case-sensitive.


## CI/CD Pipeline for code
This project uses CI/CD pipelines to automate the testing, building, and deployment processes. The main CI/CD tool employed is [GitHub Actions], and the configuration is stored in [`.github/workflows/main.yaml`, `.github/workflows/docs.yaml`].

### Continuous Integration (CI)

The CI pipeline is triggered on every push to the main branch or when pull requests are submitted. The CI process includes the following steps:

1. **Linting**: The code is checked for style and formatting using [Flaker8].
2. **Formatting**: The code is formatted using [Black].
3. **Spelling Check**: The code is spellchecked using [codespell]
4. **Unit Tests**: Unit tests are executed to ensure the code functions as expected. [Pytest]
5. **Integration Test**: Integration are executed to ensure the CLI App as expected. [Typer.CliRunner]

### Continuous Deployment (CD)

The CD pipeline is triggered when changes are merged into the main branch, and it is responsible for deploying the application. The deployment process typically involves the following steps:

1. **Build**: The application is built to create deployable artifacts.
2. **Deployment to Staging**: The application is deployed to a staging environment for further testing.
3. **End-to-End Tests**: [Optional] Automated end-to-end tests may be performed in the staging environment.
4. **Deployment to Production**: Upon successful testing, the application is deployed to the production environment.

## Documentation

This project's documentation is automatically generated using Sphinx and integrated into the CI/CD pipeline. The documentation includes details about the API, code structure, and usage.

### API Documentation

The API documentation is generated from docstrings in the source code. Sphinx extracts these docstrings and formats them into a user-friendly documentation website. To view the latest documentation, visit [Documentation Link].

### Generation in CI/CD Pipeline

The documentation is automatically generated and deployed as part of the CI/CD pipeline when a commit is pushed to the `main` branch. The main steps in the CI/CD pipeline related to documentation are as follows:

1. **Documentation Build**: Sphinx is used to build the documentation from the source code.
2. **Artifact Storage**: The generated documentation artifacts are stored, making them accessible for further steps.
3. **Deployment**: The documentation is deployed to Netlify. Please see [here](https://unit-grader-api-docs.netlify.app/)

### Viewing the Documentation Locally

To build and view the documentation locally, follow these steps:

```bash
# Install Sphinx (if not already installed)
pdm install
# Lint, format code and build api docs
pre-commit run --all-files
# Change to the 'docs' directory
cd docs
# Open the generated HTML files in a browser
open _build/html/index.html
```

## Contributing Guideline
We welcome contributions! Please follow our [contribution guidelines](.github/CONTRIBUTING.md).

## Licence
This project is licensed under the [MIT License](https://opensource.org/license/mit).