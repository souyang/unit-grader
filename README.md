# Unit Conversion Grader

## Overview
Unit Conversion Grader a command-line interface (CLI) program that allows you to convert among units of measurement and grade the users response to determine the result.

## Documentation
Please refer to docs/

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

## Command Usage

### General Instruction
- You must be able to provide `input-value`, `from-unit`, `to-unit`, `student-response` as input.
- `from-unit` and `to-unit` must be in the same unit meansurement category.
- Expected output: `correct`, `incorrect`, `invalid`.
- Supported unit meansurement categories includes `temperature` and `volumns`.
- units supported in `temperature` category: `Kelvin`, `Celsius`, `Fahrenheit` and `Rankine`. 
- units supported in `volume` category: `liters`, `tablespoons`, `cubic-inches`, `cups`, `cubic-feet`, `gallons`.
- Name of each unit is case sensitive.
- Student's response must match the correct answer after both value are rounded to the `tenths place`.

### Get help information
- Run `unit-grader --help` to get information

### Get the app version
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

