import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a yaml file and returns

    Args:
        path_to_yaml (str): Path like input

    Raises:
        ValueError: If the yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
        
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """Create list of directories

    Args:
        path to_directories (list): List of directories to create
        ignore_log (bool, optional): ignore if multiple dirs are to be created. Defaults to Fale.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok = True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file in KB

    Args:
        path (str): Path to file
        
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"
            
    
