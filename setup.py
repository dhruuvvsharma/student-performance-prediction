from setuptools import setup, find_packages
from pathlib import Path


def get_requirements():
    requirements_path = Path("requirement.txt")

    with open(requirements_path, "r") as file:
        requirements = file.readlines()

    requirements = [
        requirement.strip()
        for requirement in requirements
        if requirement.strip() and not requirement.startswith("-e")
    ]

    return requirements


setup(
    name="student-performance-prediction",
    version="0.0.1",
    author="Dhruv",
    description="End-to-end ML system for student performance prediction",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements(),
)