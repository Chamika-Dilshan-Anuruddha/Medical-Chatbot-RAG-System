import sys
from MedicalChatbot.logging import logger
from MedicalChatbot.exception import CustomException
from MedicalChatbot.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from MedicalChatbot.pipeline.stage_02_data_validation import DataValidationPipeline
from MedicalChatbot.pipeline.stage_03_data_transformatin import DataTransformationPipeline
from MedicalChatbot.pipeline.stage_04_model_trainer import ModelTrainerPipeline


STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<\n\n")
except Exception as e:
    raise CustomException(e,sys)



STAGE_NAME = "Data Validation"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<\n\n")
except Exception as e:
    raise CustomException(e,sys)



STAGE_NAME = "Data Transformation"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<\n\n")
except Exception as e:
    raise CustomException(e,sys)



STAGE_NAME = "Model Trainer"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
    obj = ModelTrainerPipeline()
    agent, model_trainer = obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<\n\n")
except Exception as e:
    raise CustomException(e,sys)