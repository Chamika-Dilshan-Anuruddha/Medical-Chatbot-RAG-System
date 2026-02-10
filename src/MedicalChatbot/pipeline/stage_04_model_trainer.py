import sys
from MedicalChatbot.components.model_trainer import ModelTrainer
from MedicalChatbot.config.configuration import ConfiguraitonManager
from MedicalChatbot.exception import CustomException
from MedicalChatbot.logging import logger


STAGE_NAME = "Model Trainer"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfiguraitonManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        agent = model_trainer.get_agent()

        #user_query = "What is IBD ?"
        #result = model_trainer.get_result(user_query,agent)
        return agent,model_trainer
    
     
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<")
        obj = ModelTrainerPipeline()
        agent,model_trainer = obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>> stage: {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<\n\n")
    except Exception as e:
        raise CustomException(e,sys)
