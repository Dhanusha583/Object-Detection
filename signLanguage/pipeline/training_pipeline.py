import sys, os
from signLanguage.logger import logging
from signLanguage.exception import SignException
# # from signLanguage.components.data_ingestion import DataIngestion
# import signLanguage.components.data_ingestion
# print("DataIngestion module location:", signLanguage.components.data_ingestion.__file__)
from signLanguage.components.data_ingestion import DataIngestion
# print("DataIngestion class loaded:", DataIngestion)





from signLanguage.entity.config_entity import (DataIngestionConfig)
                                            #    DataValidationConfig,
                                            #    ModelTrainerConfig,
                                            #    ModelPusherConfig


from signLanguage.entity.artifacts_entity import (DataIngestionArtifact)
                                                #   DataValidationArtifact,
                                                #   ModelTrainerArtifact,
                                                #   ModelPusherArtifacts)
class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        # self.data_validation_config = DataValidationConfig()
        # self.model_trainer_config = ModelTrainerConfig()
        # self.model_pusher_config = ModelPusherConfig()
        # self.s3_operations = S3Operation()

    

    def start_data_ingestion(self)-> DataIngestionArtifact:
        try: 
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config =  self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise SignException(e, sys)
        
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            # data_validation_artifact = self.start_data_validation(
            #     data_ingestion_artifact=data_ingestion_artifact
            # )

            # if data_validation_artifact.validation_status == True:
            #     model_trainer_artifact = self.start_model_trainer()
            #     model_pusher_artifact = self.start_model_pusher(model_trainer_artifact=model_trainer_artifact,s3=self.s3_operations)

            # else:
            #     raise Exception("Your data is not in correct format")


        except Exception as e:
            raise SignException(e, sys)