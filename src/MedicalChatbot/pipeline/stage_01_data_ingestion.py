import sys
from MedicalChatbot.components.data_ingestion import DataIngestion
from MedicalChatbot.config.configuration import ConfiguraitonManager
from MedicalChatbot.exception import CustomException
from MedicalChatbot.logging import logger


STAGE_NAME = "Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfiguraitonManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.copy_data()
     

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<\n\n")
    except Exception as e:
        raise CustomException(e,sys)
