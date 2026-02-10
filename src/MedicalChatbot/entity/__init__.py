from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    data_path: Path
    original_data_path: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    data_path: Path
    data_ingestion_path: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_validation_path: Path
    vectorstore_path: Path
    embedding_model_name: str
    chunk_size: int
    chunk_overlap: int

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    vectorstore_path: Path
    model_name: str