from MedicalChatbot.constants import *
from MedicalChatbot.utils import read_yaml, create_directories
from MedicalChatbot.entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig

class ConfiguraitonManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir = Path(config.root_dir),
            data_path = Path(config.data_path),
            original_data_path = Path(config.original_data_path)
        )
        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])
        data_validation_config = DataValidationConfig(
            root_dir = Path(config.root_dir),
            data_path = Path(config.data_path),
            data_ingestion_path = Path(config.data_ingestion_path),
        )
        return data_validation_config
    

    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_confg = DataTransformationConfig(
            root_dir = Path(config.root_dir),
            data_validation_path = Path(config.data_validation_path),
            vectorstore_path = Path(config.vectorstore_path),
            embedding_model_name = config.embedding_model_name,
            chunk_size = self.params.CHUNK_SIZE,
            chunk_overlap = self.params.CHUNK_OVERLAP
        )
        return data_transformation_confg
    
    def get_model_trainer_config(self)->ModelTrainerConfig:
        config = self.config.model_trainer
        create_directories([config.root_dir])
        model_trainer_cofig = ModelTrainerConfig(
            root_dir = Path(config.root_dir),
            vectorstore_path = Path(config.vectorstore_path),
            model_name = config.model_name
        )
        return model_trainer_cofig

