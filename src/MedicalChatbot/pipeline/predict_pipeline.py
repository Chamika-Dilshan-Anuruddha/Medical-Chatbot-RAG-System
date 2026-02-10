import sys
import os
from MedicalChatbot.components.model_trainer import ModelTrainer
from MedicalChatbot.exception import CustomException
from MedicalChatbot.logging import logger
from MedicalChatbot.pipeline.stage_04_model_trainer import ModelTrainerPipeline



class CustomData:
    def __init__(self,query):
        self.query = query

    def get_preprocessed_data(self):
        preprocessed_data = {
            "query":self.query
        }
        return preprocessed_data
    
class PredictPipeline:
    def __init__(self):
        pass

    def get_result(self,query_dict,agent,model_trainer:ModelTrainer):
        try:
            user_query = query_dict["query"]
            result = model_trainer.get_result(user_query,agent)
            return result
        except Exception as e:
            raise CustomException(e,sys)