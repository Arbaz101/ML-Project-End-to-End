We will maintain multiple structure for configuration of pipeline or artifact

Artifact is defined for each component pipeline

DataIngestionArtifact  - output of dataingestion step
DataValidationArtifact
DataTransformationArtifact
ModelTrainerArtifact
ModelEvaluationArtifact
ModelPusherArtifact


Create named tuple for the configuration of each step and maintain the keys of the configuration
the values for the named tuple will be read from config.yml file in config folder outside



