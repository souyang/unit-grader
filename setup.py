from setuptools import setup, find_packages

# Define the project name and version
project_name = "unit-conversion-cli"
version = "1.0.0"

# Load the README for your project's long description
with open("README.md", "r") as f:
    long_description = f.read()

# Define project dependencies
install_requires = [
    "typer",
]

setup(
    name=project_name,
    version=version,
    description="A CLI tool for grading unit conversion exam.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="xi ouyang",
    author_email="simonouyang@gmail.com",
    url="https://github.com/souyang/unit-conversion-cli",
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "simon-unit-convert-grader = unit_conversion_grader.cli:app",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
)
