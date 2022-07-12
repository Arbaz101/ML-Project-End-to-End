from asyncore import read

from sklearn import preprocessing
from Housing.logger import logging
from Housing.exception import HousingException
from Housing.entity.config_entity import DataTransformationConfig
from Housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact
from Housing.util.util import read_yaml_file, save_numpy_array_data, save_object, load_numpy_array_data, load_data
import sys,os
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from Housing.constant import *


class FeatureGenerator(BaseEstimator, TransformerMixin):
  def __init__(self, add_bedrooms_per_room=True,
                 total_rooms_ix=3,
                 population_ix=5,
                 households_ix=6,
                 total_bedrooms_ix=4, columns=None):
        """
        FeatureGenerator Initialization
        add_bedrooms_per_room: bool
        total_rooms_ix: int index number of total rooms columns
        population_ix: int index number of total population columns
        households_ix: int index number of  households columns
        total_bedrooms_ix: int index number of bedrooms columns
        """
        try:
            self.columns = columns
            if self.columns is not None:
                total_rooms_ix = self.columns.index(COLUMN_TOTAL_ROOMS)
                population_ix = self.columns.index(COLUMN_POPULATION)
                households_ix = self.columns.index(COLUMN_HOUSEHOLDS)
                total_bedrooms_ix = self.columns.index(COLUMN_TOTAL_BEDROOM)

            self.add_bedrooms_per_room = add_bedrooms_per_room
            self.total_rooms_ix = total_rooms_ix
            self.population_ix = population_ix
            self.households_ix = households_ix
            self.total_bedrooms_ix = total_bedrooms_ix
        except Exception as e:
            raise HousingException(e, sys) from e
  
  def fit(self, X, y=None):
        return self

  def transform(self, X, y=None):
      try:
          room_per_household = X[:, self.total_rooms_ix] / \
                                X[:, self.households_ix]
          population_per_household = X[:, self.population_ix] / \
                                      X[:, self.households_ix]
          if self.add_bedrooms_per_room:
              bedrooms_per_room = X[:, self.total_bedrooms_ix] / \
                                  X[:, self.total_rooms_ix]
              generated_feature = np.c_[
                  X, room_per_household, population_per_household, bedrooms_per_room]
          else:
              generated_feature = np.c_[
                  X, room_per_household, population_per_household]

          return generated_feature
      except Exception as e:
          raise HousingException(e, sys) from e

class DataTransformation:
  
  def __init__(self,  data_transformation_config: DataTransformationConfig,
      data_ingestion_artifact: DataIngestionArtifact,
      data_validation_artifact: DataValidationArtifact):
    try:
      self.data_transformation_config = data_transformation_config
      self.data_ingestion_artifact = data_ingestion_artifact
      self.data_validation_artifact = data_validation_artifact
    except Exception as e:
      raise HousingException(e,sys) from e
  
    
  def get_data_transformer_object(self)->ColumnTransformer:
    try:
      schema_file_path = self.data_validation_artifact.schema_file_path
      
      dataset_schema = read_yaml_file(file_path=schema_file_path)
      
      numerical_columns = dataset_schema[NUMERICAL_COLUMNS_KEY]
      categorical_columns = dataset_schema[CATEGORICAL_COLUMNS_KEY]
      
      num_pipeline = Pipeline(steps = [
        ('imputer', SimpleImputer(strategy='median')),
        ('feature_generator', FeatureGenerator(add_bedrooms_per_room = self.data_transformation_config.add_bedroom_per_room,
                                               columns=numerical_columns)),
        ('scalar', StandardScaler())
      ])
      
      cat_pipeline = Pipeline(steps=[
        ('impute', SimpleImputer(strategy='most_frequent')),
        ('one_hot_encoder', OneHotEncoder()),
        ('scaler', StandardScaler(with_mean=False))
      ])
      
      logging.info(f'Categorical_columns: {categorical_columns}')
      logging.info(f'Numerical_columns: {numerical_columns}')
      
      preprocessing = ColumnTransformer([
        ('num_pipeline', num_pipeline, numerical_columns),
        ('cat_pipeline', cat_pipeline, categorical_columns)
      ])
      
      return preprocessing
    except Exception as e:
      raise HousingException(e,sys) from e
    
  
  def initiate_data_transformation(self)->DataTransformationArtifact:
    try:
      preprocessing_obj = self.get_data_transformer_object()
      
      
    except Exception as e:
      raise HousingException(e, sys) from e