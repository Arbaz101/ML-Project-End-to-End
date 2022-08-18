from Housing.pipeline import Pipeline
from Housing.exception import HousingException
from Housing.logger import logging
from Housing.config.configuration import Configuartion
from Housing.component.datasformation import DataTransformation
import os
def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()