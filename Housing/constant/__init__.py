from Housing.util.util import read_yaml_file

import os
from datetime import datetime

ROOT_DIR = os.getcwd()


CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)


CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


#Training pipeline related variable 
#mapping the keys from YAML file into a variable in python
# the values on RHS are the keys from  config.yml file 
TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = 'artifact_dir'
TRAINING_PIPELINE_NAME_KEY = 'pipeline_name'

#Constants for data ingestion
DATA_INGESTION_CONFIG_KEY = 'data_ingestion_config'
DATA_INGESTION_ARTIFACT_DIR = 'data_ingestion'
DATA_INGESTION_DOWNLOAD_URL_KEY = 'dataset_download_url'
DATA_INGESTION_RAW_DATA_DIR_KEY = 'raw_data_dir'
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = 'tgz_download_dir'
DATA_INGESTION_INGESTED_DIR_NAME_KEY = 'ingested_dir'
DATA_INGESTION_TRAIN_DIR_KEY = 'ingested_train_dir'
DATA_INGESTION_TEST_DIR_KEY = 'ingested_test_dir'

#Data Validation related variable
DATA_VALIDATION_CONFIG_KEY = 'data_validation_config'
DATA_VALIDATION_SCHEMA_FILE_NAME = 'schema_file_name'
DATA_VALIDATION_SCHEMA_DIR_KEY = 'schema_dir'
DATA_VALIDATION_ARTIFACT_DIR_NAME = 'data_validation'
DATA_VALIDATION_REPORT_FILE_PATH_KEY = 'report_file_path'
DATA_VALIDATION_REPORT_PAGE_FILE_PATH_KEY = 'report_page_file_path'

#Data Transformation 
DATA_TRANSFORMATION_ARTIFACT_DIR = 'data_transformation'
DATA_TRANSFORMATION_CONFIG_KEY = 'data_transformation_config'
DATA_TRANSFORMATION_ADD_BEDROOM_PER_ROOM_KEY =  'add_bedroom_per_room'
DATA_TRANSFORMATION_TRANSFORMED_DIR_KEY = 'transformed_dir'
DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR_KEY = 'transformed_train_dir'
DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR_KEY = 'transformed_test_dir'
DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY = 'preprocessing_dir'
DATA_TRANSFORMATION_PREPROCESSED_FILE_NAME_KEY = 'preprocessed_object_file_name'
COLUMN_TOTAL_ROOMS = 'total_rooms'
COLUMN_POPULATION = 'population'
COLUMN_HOUSEHOLDS = 'households'
COLUMN_TOTAL_BEDROOM = 'total_bedrooms'
DATASET_SCHEMA_COLUMNS_KEY = 'columns'

NUMERICAL_COLUMNS_KEY = 'numerical_columns'
CATEGORICAL_COLUMNS_KEY = 'categorial_columns'