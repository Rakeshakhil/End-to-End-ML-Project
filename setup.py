# importing the required modules
from setuptools import find_packages, setup
from typing import List
# defining the required modules from requirements.txt
requirements_file_name = 'requirements.txt'
REMOVE_PACKAGE = '-e .'



def get_requirements() -> List[str]:
    with open(requirements_file_name) as requirement_file:
        requirements_list = requirement_file.readlines()
    requirements_list = [requirement_name.strip() for requirement_name in requirements_list if requirement_name.strip() and not requirement_name.startswith('#')]
    if REMOVE_PACKAGE in requirements_list:
        requirements_list.remove(REMOVE_PACKAGE)
    return requirements_list



# This code is from setup file from python.org.
setup(name='Insurance',
      version='0.0.1',
      description='Insurance Industrial Level Project',
      author='Rakesh M',
      author_email='rakei9820@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements()
      )