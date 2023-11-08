# Unit Conversion Grader

Unit Conversion Grader a command-line interface (CLI) program that allows you to convert among units of measurement and grade the users response to determine the result.

## Setup

Choose either **stable** or **development**.

For **stable** release:

- `python -m pip install unit-grader`

For **development**:
- `brew install pdm`
- `git clone https://github.com/souyang/unit-grader.git`
- `cd unit-grader`
- `pdm venv create --with venv 3.9`
- `python3 -m pip install -e .`

# Usage

## Constraints
- `from-unit` and `to-unit` must be in the same unit meansurement category
- Supported unit meansurement categories includes `temperature` and `volumns`
- units supported in `temperature` category: `Kelvin`, `Celsius`, `Fahrenheit` and `Rankine` 
- units supported in `volume` category: `liters`, `tablespoons`, `cubic-inches`, `cups`, `cubic-feet`, `gallons`
- Name of unit is case sensitive

## Understand the usage
- Run `unit-grader --help` to get information

## Grade the student response based on inputs

- `unit-grader` has four required fields
  - `input-value`: a numeric value
  - `from-unit`: a measurement unit to convert
  - `to-unit`
  - `student response` 
- run `unit-grader` with all the required fields
  - For example: `unit-grader -i 50  -f Kelvin -t Celsius -s 30` 
