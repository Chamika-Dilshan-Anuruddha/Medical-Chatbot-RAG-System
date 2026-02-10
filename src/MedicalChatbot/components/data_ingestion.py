import os
from MedicalChatbot.logging import logger
import shutil
from MedicalChatbot.entity import DataIngestionConfig
from MedicalChatbot.utils import create_directories


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_data(self):
        print("Data downloaded successfully")
        logger.info("Data downloaded successfully...")
    
    def copy_data(self):
        source_dirpath  = self.config.original_data_path
        destination_dirpath = self.config.data_path
        create_directories([destination_dirpath])
        files = os.listdir(source_dirpath)
        for file in files:
            file_type = file.split(".")[-1].lower()
            if file_type == "pdf":
                shutil.copy(os.path.join(source_dirpath,file),destination_dirpath)
        logger.info("Data copied successfully...")