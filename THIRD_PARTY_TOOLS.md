# Third-Party Tools

In the development of this project, we've leveraged the following third-party tools to enhance functionality and streamline development:

## PDM

PDM is a Python project management tool and package installer. It simplifies the process of managing project dependencies and virtual environments.

### Why we choose PDM

We chose PDM for its modern and efficient dependency management, which allows for faster and more reliable project setups. It provides features like parallel installations, deterministic builds, and improved performance compared to traditional package managers.

### Comparison with other tools
- PDM is PEP compliant using pyproject.toml and lockfile specification.
- PDM could automatically resolve the package version to make it compatible with target python versions  
- PDM has the option to run custom shell scripts and make the development much simple
- PDM is 90% faster than `Pipenv` and 68% faster than `Poetry` regarding installing dependencies with cache and reuse lockfile.
- You can group your development dependencies in group for better package orgnaization


## Typer

Typer is a Python library for building command-line applications with a focus on simplicity and efficiency.

### Why we choose Typer

Typer was selected for its clean and intuitive syntax, making it easy to build powerful command-line interfaces with less boilerplate code. Its automatic documentation generation and support for type hints contribute to a more maintainable and user-friendly CLI.

### Comparison with other tools
- Less boilerplate code when compared with `Argparse` and is developer friendly.
- Integration with Python type hints for better code readability and type checking when compared with `Click`.
- Typer's CliRunner provides a convenient way to simulate command-line input and output for integration testing without any external process when compared with `Argparse` and `Click`. 

## Tomli
Tomli is a Python library for parsing TOML. It is fully compatible with TOML v1.0.0.

### Why we choose Tomli
It is 100% spec compliant and is the fastest pure Python parson with no dependencies and it could solve the issue of importlib.metadata output local version identifier (such as +editable)

### Comparison with other tools
- It is pure Python with zero dependencies
- It is 16x faster than tomlkit and 2.3x faster than toml
- It eliminate the local veresion identifier (such as +editable) when output version

## Pre-Commit

Pre-Commit is a framework for managing and maintaining multi-language pre-commit hooks.

### Why we choose Pre-Commit

Pre-Commit is an excellent choice for enforcing code quality and consistency. By using pre-commit hooks, we ensure that code formatting, linting, and other checks are applied automatically before each commit, contributing to a cleaner and more consistent codebase.

### Comparison with other tools
- It is a general-purpose framework that can be used for various checks and tasks across multiple languages
- It is more flexible and can accommodate a wide range of hooks and tools for different purposes even for custom hooks in local repo when compared with `trailer`
- It has a larger and more active community, with extensive documentation and integration with various tools when compared with `trailer`

## Pytest

Pytest is a testing framework for Python that makes it easy to write simple unit tests as well as complex functional tests.

### Why we choose Pytest

Pytest is widely recognized for its simplicity, scalability, and powerful features. It allows us to write expressive and maintainable tests, supports fixtures, and provides detailed test reports, making it an ideal choice for testing our project.

### Comparison with other tools
- Automatically discovers test files and test cases without requiring explicit subclassing or naming conventions whilst `unittest` follows stricter discover mechanism.
- pytest provides clear and expressive failure messages with detailed information on what went wrong. Its assertion introspection helps in quickly identifying issues whilst `unittest`'s failure message might not be as informative.

## Ruff
Ruff is a fast Linter as the replacement of Flake8, isort, black for both linting and formatting the code.

### Why we choose Ruff
Ruff, offers unparalleled speed, being 10-100 times faster than existing linters and formatters. Ruff provides a powerful and efficient solution for code linting and formatting replacing `Flake8`, `Black` and `isort` while supporting configuration through pre-commit and pyproject.toml.

### Comparison with other tools
- 10-100 times faster than existing linter and formatters such as `Flake8` and `Black`.
- Support for pyproject.toml, built-in caching, automatic error correction when compared with `Flake8`.
- Support over 700+ built-in rules inclidng Flake8 plugins flake8-bugbear.
- Could replace `Flake8`, `Black` and `isort` as all-in-one for formatting and linting.

## Sphinx

Sphinx is a documentation generator for Python projects.

### Why we choose Sphinx

Sphinx is a robust documentation tool that integrates seamlessly with Python projects. Its support for reStructuredText and the ability to generate various output formats make it an ideal choice for creating clear and well-structured project documentation.

### Comparison with other tools
- Sphinx has rich ecosystem of extensions and themes that make the documentation highly customizable when compared with `MkDocs`
- Sphinx could support generating PDF or ePub besides HTML and could suit will with extenstive API documentation for future maintainance when compared with `MkDocs`