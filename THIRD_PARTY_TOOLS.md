# Third-Party Tools

In the development of this project, we've leveraged the following third-party tools to enhance functionality and streamline development:

## PDM

[PDM](https://pdm-project.org/latest/) is a Python project management tool and package installer. It simplifies the process of managing project dependencies and virtual environments.

### Why choose PDM

We chose [PDM](https://pdm-project.org/latest/) for its modern and efficient dependency management, which allows for faster and more reliable project setups. It provides features like parallel installations, deterministic builds, and improved performance compared to traditional package managers. It also could auto correct the package version to make it compatible with target python versions.

### Comparison with other tools

- [PDM](https://pdm-project.org/latest/) is PEP compliant using pyproject.toml and lockfile specification.
- [PDM](https://pdm-project.org/latest/) could automatically resolve the package version to make it compatible with target Python versions. 
- [PDM](https://pdm-project.org/latest/) has the option to run custom shell scripts and make the development and devop scripts much simpler.
- [PDM](https://pdm-project.org/latest/) is 90% faster than [Pipenv](https://pipenv.pypa.io/en/latest/) and 68% faster than [Poetry](https://www.poetryfoundation.org/) regarding installing dependencies with cache and reuse lockfile.


## Typer

Typer is a Python library for building command-line applications with a focus on simplicity and efficiency.

### Why choose Typer

[Typer](https://typer.tiangolo.com/) was selected for its clean and intuitive syntax, making it easy to build powerful command-line interfaces with less boilerplate code. Its automatic documentation generation and support for type hints contribute to a more maintainable and user-friendly CLI.

### Comparison with other tools
- Less boilerplate code when compared with [Argparse](https://docs.python.org/3/library/argparse.html) and is developer-friendly.
- Integration with Python type hints for better code readability and type checking when compared with [Click](https://click.palletsprojects.com/).
- [Typer](https://typer.tiangolo.com/)'s CliRunner provides a convenient way to simulate command-line input and output for integration testing without any external process when compared with [Argparse](https://docs.python.org/3/library/argparse.html) and [Click](https://click.palletsprojects.com/). 

## pre-commit

Pre-Commit is a framework for managing and maintaining multi-language pre-commit hooks.

### Why choose pre-commit

[pre-commit](https://pre-commit.com/) is an excellent choice for enforcing code quality and consistency. By using pre-commit hooks, we ensure that code formatting, linting, and other checks are applied automatically before each commit, contributing to a cleaner and more consistent codebase.

### Comparison with other tools
- It is a general-purpose framework that can be used for various checks and tasks across multiple languages when compared with [Lint-Staged](https://github.com/lint-staged/lint-staged) and [Husky](https://typicode.github.io/husky/) for JavaScript only.
- It is more flexible and can accommodate a wide range of hooks and tools for different purposes even for custom hooks in local repo when compared with [overcommit](https://github.com/sds/overcommit)
- It has a larger and more active community, with extensive documentation and integration with various tools when compared with [overcommit](https://github.com/sds/overcommit)

## Pytest

[Pytest](https://docs.pytest.org/) is a testing framework for Python that makes it easy to write simple unit tests as well as complex functional tests.

### Why choose Pytest

Pytest is widely recognized for its simplicity, scalability, and powerful features. It allows us to write expressive and maintainable tests, supports fixtures, and provides detailed test reports, making it an ideal choice for testing our project.

### Comparison with other tools
- Automatically discovers test files and test cases without requiring explicit subclassing or naming conventions whilst [unittest](https://docs.python.org/3/library/unittest.html) follows stricter discover mechanism.
- [Pytest](https://docs.pytest.org/) provides clear and expressive failure messages with detailed information on what went wrong. Its assertion introspection helps in quickly identifying issues whilst [unittest](https://docs.python.org/3/library/unittest.html)'s failure message might not be as informative.

## Ruff
Ruff is a fast Linter as the replacement of Flake8, isort, black for both linting and formatting the code.

### Why choose Ruff
[Ruff](https://docs.astral.sh/ruff), offers unparalleled speed, being 10-100 times faster than existing linters and formatters. [Ruff](https://docs.astral.sh/ruff) provides a powerful and efficient solution for code linting and formatting replacing [Flake8](https://flake8.pycqa.org/en/latest/), [Black](https://github.com/psf/black) and [isort](https://pycqa.github.io/isort/) while supporting configuration through [pre-commit](https://pre-commit.com/) hook and pyproject.toml.

### Comparison with other tools
- 10-100 times faster than existing linter and formatters such as `Flake8` and `Black`.
- Support for pyproject.toml, built-in caching, automatic error correction when compared with `Flake8`.
- Support over 700+ built-in rules inclidng Flake8 plugins flake8-bugbear.
- Could replace `Flake8`, `Black` and `isort` as all-in-one for formatting and linting.

## codespell
[codespell](https://github.com/codespell-project/codespell) is a light-weight and fast tool catch spelling mistakes in code.

### Why choose codespell
It is simple and fast and could quickly identify the common spelling errors and it is lightweight addition to CI/CD.

### Comparison with other tools
It is much light weight and fast when compared with [pyspelling](https://facelessuser.github.io/pyspelling/) and is ideal tool for pre-commit hook and CI/CD pipeline.

## Sphinx

Sphinx is a documentation generator for Python projects.

### Why choose Sphinx

[Sphinx](https://www.sphinx-doc.org/) is a robust documentation tool that integrates seamlessly with Python projects. Its support for reStructuredText and the ability to generate various output formats make it an ideal choice for creating clear and well-structured project documentation.

### Comparison with other tools
- [Sphinx](https://www.sphinx-doc.org/) has rich ecosystem of extensions and themes that make the documentation highly customizable when compared with [MkDocs](https://www.mkdocs.org/).
- [Sphinx](https://www.sphinx-doc.org/) could support generating PDF or ePub besides HTML and could suit will with extenstive API documentation for future maintenance when compared with [MkDocs](https://www.mkdocs.org/).

## bump-my-version
A small command line tool to simplify releasing software by updating all version strings in code by the correct increment and optionally commit and tag the changes.

### Why choose bump-my-version

[bump-my-version](https://github.com/callowayproject/bump-my-version) is a robust simple tool that simplifying the release with auto increment the version number

### Comparison with other tools
- It is build system independent when compared with `setuptools-scm` depending on `setuptools` build system.
- It is actively maintained when compared with `bumpversion`, `bump2version` and `standard-version`.
- It could update the version directly in configuration files whereas alternative tool such as `versioneer` cannot change configuration files and use the source code files such as `__init__.py` to control the version.
 