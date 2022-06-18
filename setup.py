from setuptools import setup
from typing import List

project_name = "housing-predictor"
version = "0.0.1"
author = "Arbaz"
description = "This is a House Price prediction project"
packages = ['housing']

requirement_file_name = 'requirements.txt'

def get_requirements_list():
  """
  Description: This function is going to return list of requirement mention in requirements.txt files
  
  return name of libraries mentioned in requirements.txt file
  """
  with open(requirement_file_name) as requirement_file:
    return requirement_file.readlines()


setup(
  name = project_name,
  version= version,
  author = author,
  description=description,
  packages= packages,
  install_requires = get_requirements_list()
)
