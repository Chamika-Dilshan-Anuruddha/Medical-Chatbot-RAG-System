import sys
from MedicalChatbot.components.data_transformation import DataTransformation
from MedicalChatbot.config.configuration import ConfiguraitonManager
from MedicalChatbot.exception import CustomException
from MedicalChatbot.logging import logger


STAGE_NAME = "Data Transformation"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfiguraitonManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        docs = data_transformation.load_pdf_documents()
        all_splits = data_transformation.split_pdf_loaded_documents(docs)
        #vector_store = data_transformation.create_and_save_vectorstore(all_splits)
        #vector_store = data_transformation.get_saved_vectorsote()
     

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<\n\n")
    except Exception as e:
        raise CustomException(e,sys)
