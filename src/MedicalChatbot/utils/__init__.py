import os
import sys
from pathlib import Path
from box import ConfigBox
import yaml
from MedicalChatbot.exception import CustomException
from MedicalChatbot.logging import logger

def read_yaml(filepath:Path)->ConfigBox:
    try:
        with open(filepath) as f:
            content = yaml.safe_load(f)
        content = ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)
    return content


def create_directories(paths:list[Path]):
    try:
        for path in paths:
            os.makedirs(path, exist_ok=True)
    except Exception as e:
        raise CustomException(e,sys)