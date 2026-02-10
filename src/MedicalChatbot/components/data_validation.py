import os
from MedicalChatbot.logging import logger
import shutil
from MedicalChatbot.entity import DataValidationConfig
from MedicalChatbot.utils import create_directories

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config

    def data_validation(self):
        source_dirpath = self.config.data_ingestion_path
        destination_dirpath = self.config.data_path
        create_directories([destination_dirpath])
        files = os.listdir(source_dirpath)
        for file in files:
            shutil.copy(os.path.join(source_dirpath,file),destination_dirpath)
        logger.info("Data validation completed...")