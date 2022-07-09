from Housing.pipeline import pipeline
from Housing.config import configuration


def main():
  try:
    pipe = pipeline()
    pipe = pipeline.run_pipeline()
      # config = configuration.Configuration()
      # config.get_data_validation_config()
    #print(config)
  except Exception as e:
      print(e)
      
if __name__ == '__main__':
  main()