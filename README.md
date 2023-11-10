# Unit Conversion Grader

## Overview
Unit Conversion Grader a command-line interface (CLI) program that allows you to convert among units of measurement and grade the users response to determine the result.

## Installation

Choose either **stable** or **development**.

### Stable

- `python -m pip install unit-grader`

### Development
- `brew install pdm`
- `git clone https://github.com/souyang/unit-grader.git`
- `cd unit-grader`
- `pdm venv create --with venv 3.9`
- `python3 -m pip install -e .`

## Command Usage

### Syntax
```bash
unit-grader -i <input-value> -f <from-unit> -t <to-unit> -s <student-response>
```

### General Instructions
- Provide `input-value`, `from-unit`, `to-unit`, `student-response` as input.
- `from-unit` and `to-unit` must be in the same unit meansurement category.
- Expected output: `correct`, `incorrect`, `invalid`.
- Supported unit meansurement categories include `temperature` and `volumns`.
- units supported in `temperature` category: `Kelvin`, `Celsius`, `Fahrenheit` and `Rankine`. 
- units supported in `volume` category: `liters`, `tablespoons`, `cubic-inches`, `cups`, `cubic-feet`, `gallons`.
- Name of each unit is case sensitive.
- Student's response must match the correct answer after both value are rounded to the tenths place.

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
You can get the detail information of your input in verbose mode
For example, `unit-grader -i 100  -f Kelvin -t dog -s -173.15 -v` will print out the messages

```
Verbose mode is enabled.
input-value: 100
from_unit: Celsius
to_unit: Kelvin
student_response: 305.2
```

### Error Handling
| Use Case | Sample Command | Expected Message Reported to user
| ---------|----------|----------|
| `Input numeric value` is not a number | `unit-grader -i dog  -f Kelvin -t Celsius -s -173.15` | Input Error: dog as input_value needs to be a number. Please use --help to see valid options.
| `Input unit of measure` is not supproted or invalid | `unit-grader -i 100  -f Test -t Celsius -s -173.15` | Input Error: Test as from_unit is not supported. Select a conversion unit (Kelvin, Celsius,Fahrenheit,Rankine for temperature; liters, tablespoons, cubic-inches, cups, cubic-feet, gallons for volume). Please note that the unit is case-sensitive.
| `Target unit of measure` is not supproted or invalid | `unit-grader -i 100  -f Test -t Celsius -s -173.15` | Input Error: Test as from_unit is not supported. Select a conversion unit (Kelvin, Celsius,Fahrenheit,Rankine for temperature; liters, tablespoons, cubic-inches, cups, cubic-feet, gallons for volume). Please note that the unit is case-sensitive.
| `Input unit of measure` and `Target unit of measure` are not in the same category | `unit-grader -i 100  -f cups -t Celsius -s -173.15` | Input Error: Ensure the selected conversion units match their respective categories for a valid conversion. Select a conversion unit (Kelvin, Celsius,Fahrenheit,Rankine for temperature; liters, tablespoons, cubic-inches, cups, cubic-feet, gallons for volume). Please note that the unit is case-sensitive.


## CI/CD Pipeline for code
This project uses CI/CD pipelines to automate the testing, building, and deployment processes. The main CI/CD tool employed is [GitHub Actions], and the configuration is stored in [`.github/workflows/main.yaml`, `.github/workflows/docs.yaml`, `.github/workflows/main.yaml`].

### Continuous Integration (CI)

The CI pipeline is triggered on every push to the main branch or when pull requests are submitted. The CI process includes the following steps:

1. **Linting**: The code is checked for style and formatting using [Flaker8].
2. **Formatting**: The code is formatted using [Black].
2. **Unit Tests**: Unit tests are executed to ensure the code functions as expected. [Pytest]
3. **Integration Test**: Integration are executed to ensure the CLI App as expected. [Typer.CliRunner]

### Continuous Deployment (CD)

The CD pipeline is triggered when changes are merged into the main branch, and it is responsible for deploying the application. The deployment process typically involves the following steps:

1. **Build**: The application is built to create deployable artifacts.
2. **Deployment to Staging**: The application is deployed to a staging environment for further testing.
3. **End-to-End Tests**: [Optional] Automated end-to-end tests may be performed in the staging environment.
4. **Deployment to Production**: Upon successful testing, the application is deployed to the production environment.

## Vision



## Contributing
We welcome contributions! Please follow our contribution guidelines.

## Licence
This project is licensed under the MIT License.