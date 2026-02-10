import sys
from MedicalChatbot.components.data_validation import DataValidation
from MedicalChatbot.config.configuration import ConfiguraitonManager
from MedicalChatbot.exception import CustomException
from MedicalChatbot.logging import logger


STAGE_NAME = "Data Validation"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfiguraitonManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.data_validation()
     

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<\n\n")
    except Exception as e:
        raise CustomException(e,sys)
