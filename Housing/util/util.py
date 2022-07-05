#this util file will be used for collection of custom classes which will be used on some or the other func
import yaml
from Housing.exception import HousingException
import sys

def read_yaml_file(file_path):
  """
  Reads a YAML file and return the contents in Dictionary 

  Args:
      file_path (str): path for the yaml file

  Returns:
      dict: returns dictionary
  """
  try: 
    with open(file_path, "rb") as yaml_file:
      yml_config_info = yaml.safe_load(yaml_file)
      return yml_config_info
  except Exception as e:
    raise HousingException(e, sys) from e