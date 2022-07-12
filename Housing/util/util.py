#this util file will be used for collection of custom classes which will be used on some or the other func
import yaml
from Housing.exception import HousingException
import sys, os
import numpy as np
import dill
import pandas as pd
from Housing.constant import *

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
  
  
def save_numpy_array_data(file_path: str, array: np.array):
  """
  Save numpy array data to a file
  Args:
      file_path (str): location of file to save
      array (np.array): data to save
  """
  try:
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, 'wb') as file_obj:
      np.save(file_obj, array)
  except Exception as e:
    raise HousingException(e,sys) from e
  
  
def load_numpy_array_data(file_path: str) -> np.array:
  """
  load numpy array data from file
  Args:
      file_path (str): path to the file to load data from

  Returns:
      np.array: numpy array
  """
  try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
  except Exception as e:
      raise HousingException(e, sys) from e
    

def save_object(file_path: str, obj):
  """
  save the pkl object in the destination filepath
  Args:
      file_path (str): path where the object needs to be saved
      obj (_type_): object which needs to be saved
  """
  try:
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(filepath, 'wb') as file_obj:
      dill.dump(obj, file=file_obj)
  except Exception as e:
    raise HousingException(e, sys) from e 
  

def load_object(file_path:str):
    """
    file_path: str
    """
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise HousingException(e,sys) from e
      
    
def load_data(file_path:str, schema_file_path:str) -> pd.DataFrame:
    try:
      dataset_schema = read_yaml_file(schema_file_path)
      
      schema = dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]
      
      dataframe = pd.read_csv(file_path)
      
      
      for column in dataframe.columns:
        if column in list(schema.keys()):
          dataframe[column].astype(schema[column])
        else:
          error_message = f"{error_message} \n Column: [{column}] is not in the Schema"
      if len(error_message) > 0:
       
        raise Exception(error_message)
      return dataframe
    
    except Exception as e:
      raise HousingException(e,sys) from e