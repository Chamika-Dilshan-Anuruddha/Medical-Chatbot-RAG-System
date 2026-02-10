from langchain_huggingface import HuggingFaceEmbeddings  #type:ignore
from langchain_core.vectorstores import InMemoryVectorStore  #type:ignore
from langchain_community.document_loaders import PyPDFDirectoryLoader  #type:ignore
from langchain_text_splitters import RecursiveCharacterTextSplitter  #type:ignore
from MedicalChatbot.entity import DataTransformationConfig
from MedicalChatbot.logging import logger

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
        self.embeddings = self._get_embedding_model()
    
    def _get_embedding_model(self):
        embedding = HuggingFaceEmbeddings(model_name = self.config.embedding_model_name)
        logger.info("Embedding model retrieved...")
        return embedding
    
    def _get_inmemory_vectorstore(self,embedding):   
        vector_store = InMemoryVectorStore(embedding)
        logger.info("Vector store retrieved...")
        return vector_store
    
    def load_pdf_documents(self):
        loader = PyPDFDirectoryLoader(self.config.data_validation_path)
        docs = loader.load()
        logger.info("Documents are loaded...")
        return docs
    
    def split_pdf_loaded_documents(self,docs):

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.config.chunk_size,
            chunk_overlap=self.config.chunk_overlap,
            add_start_index=True
        )
        all_splits = text_splitter.split_documents(docs)
        logger.info("PDF loaded docs are splitted...")
        return all_splits
    
    def create_and_save_vectorstore(self,all_splits):
        vector_store = self._get_inmemory_vectorstore(self.embeddings)
        document_ids = vector_store.add_documents(all_splits)
        vector_store.dump(self.config.vectorstore_path)
        logger.info("Vector store created and stored...")
        return vector_store

    def get_saved_vectorsote(self):
        vector_store = InMemoryVectorStore.load(self.config.vectorstore_path, self.embeddings)
        logger.info("Vector store retrieved...")
        return vector_store