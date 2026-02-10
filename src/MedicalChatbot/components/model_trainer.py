from langchain.agents.middleware import dynamic_prompt #type:ignore
from langchain.agents import create_agent #type:ignore
from langchain.chat_models import init_chat_model #type:ignore
from MedicalChatbot.entity import ModelTrainerConfig
from MedicalChatbot.components.data_transformation import DataTransformation
from MedicalChatbot.config.configuration import ConfiguraitonManager
from MedicalChatbot.logging import logger
from dotenv import load_dotenv
load_dotenv()

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config = config
        self.data_transformation = self._get_data_transformation_object()
        self.model = self._get_model()

    def _get_model(self):
        model = init_chat_model(self.config.model_name)
        logger.info("LLM model is retrieved...")
        return model
    
    def _get_data_transformation_object(self):
        config_manager = ConfiguraitonManager()
        data_transformation_obj = DataTransformation(config_manager.get_data_transformation_config())
        return data_transformation_obj


    def generate_system_message(self,user_query):
        vector_store = self.data_transformation.get_saved_vectorsote()
        retrieved_docs = vector_store.similarity_search(user_query)
        docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
        system_message = (
            "Yor are a helpful assistant. Use the following context in your response:"
            f"\n\n{docs_content}"
        )
        logger.info("System prompt is generated...")
        return system_message
    

    def get_agent(self):
        agent = create_agent(self.model)
        logger.info("Agent is created...")
        return agent
    
    
    def get_result(self,query,agent):
        resulst = agent.invoke({"messages": [
            {"role":"system", "content":self.generate_system_message(query)},
            {"role":"user", "content":query}
        ]})

        client_result = resulst["messages"][-1].content
        return client_result
