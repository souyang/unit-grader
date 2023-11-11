# Contributing to Unit Grader

By participating in this project, you agree to abide by the [code of conduct](CODE_OF_CONDUCT.md).

## Getting Started

To get started with contributing, please follow these steps:

1. Fork the repository and clone it to your local machine.
2. Install any necessary dependencies.
3. Create a new branch for your changes: `git checkout -b my-branch-name`.
4. Make your desired changes or additions.
5. Run the tests to ensure everything is working as expected.
6. Commit your changes: `git commit -m "Descriptive commit message"`.
7. Push to the branch: `git push origin my-branch-name`.
8. Submit a pull request to the `main` branch of the original repository.

## Code Style

Please make sure to follow the established code style guidelines for this project. Consistent code style helps maintain readability and makes it easier for others to contribute to the project.

To enforce this we use [`pre-commit`](https://pre-commit.com/) to run [`isort`](https://pycqa.github.io/isort/), [`black`](https://black.readthedocs.io/en/stable/index.html) and [`flake8`](https://flake8.pycqa.org/en/latest/) on every commit.

`pre-commit` is part of our `pyproject.toml` file so you should already have it installed. If you don't, you can install the library via pip with:

```bash
$ pdm install

# And then install the `pre-commit` hooks with:

$ pre-commit install

# output:
pre-commit installed at .git/hooks/pre-commit
```

If you are not familiar with the concept of [git hooks](https://git-scm.com/docs/githooks) and/or [`pre-commit`](https://pre-commit.com/) please read the documentation to understand how they work.

As an introduction of the actual failed workflow, here is an example of the process you will encounter when you make a commit that is successful:
```bash
git add your_file.py
git commit -m "commit message"
Check for added large files..............................................Passed
Check for case conflicts.................................................Passed
Check JSON...........................................(no files to check)Skipped
Check for merge conflicts................................................Passed
Check for broken symlinks............................(no files to check)Skipped
Check Toml...............................................................Passed
Validate pyproject.toml..................................................Passed
Sort imports with isort....................................................................Passed
Format code with black....................................................................Failed
Check code style with flake8...................................................................Passed
- hook id: black
- files were modified by this hook
```
Now your file cannot to committed before you fix the relevant code

As an introduction of the actual successful workflow, here is an example of the process you will encounter when you make a commit that is successful:
```bash
git add your_file.py
git commit -m "commit message"
Check for added large files..............................................Passed
Check for case conflicts.................................................Passed
Check JSON...........................................(no files to check)Skipped
Check for merge conflicts................................................Passed
Check for broken symlinks............................(no files to check)Skipped
Check Toml...............................................................Passed
Validate pyproject.toml..................................................Passed
Sort imports with isort..................................................Passed
Format code with black...................................................Passed
Check code style with flake8.............................................Passed
Generate API docs........................................................Passed
```
Now your file has been committed and you can push your changes.

At the beginning this might seem like a tedious process (having to add the file again after `isort`, `black` and `flake8`, `sphinx-apidoc` have modified it) but it is actually very useful. It allows you to see what changes `sphinx-apidoc`, `black` and `issort`  have made to your files or the error message generated from `flake8`` and make sure that the related files are correct before you commit them.

## Issue Tracker

If you encounter any bugs, issues, or have feature requests, please [create a new issue](https://github.com/souyang/unit-grader/issues/new) on the project's GitHub repository. Provide a clear and descriptive title along with relevant details to help us address the problem or understand your request.

## Licensing

By contributing to Unit Grader, you agree that your contributions will be licensed under the [LICENSE](../LICENSE) file of the project.

Thank you for your interest in contributing to Unit Grader! We appreciate your support and look forward to your contributions.