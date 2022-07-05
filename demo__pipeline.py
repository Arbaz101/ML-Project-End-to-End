from Housing.pipeline import pipeline




print(code)
def main():
  try:
      pipe = pipeline()
      pipe = pipeline.run_pipeline()
  except Exception as e:
      print(e)
      
if __name__ == '__main__':
  main()