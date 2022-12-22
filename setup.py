from setuptools import find_packages,setup

# from typing import List

# REQUIREMENTS_FILE_NAME = "requirements.txt"

def get_requirements():
    pass #->List[str]:
    #with open(REQUIREMENTS_FILE_NAME) as requirement_file:

setup(
    name = "sensor",
    version = "0.0.1",
    author = "LGLV",
    author_email = "lgermanlv@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)