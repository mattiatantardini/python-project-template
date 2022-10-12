from typing import Dict
import logging
import yaml


def read_yaml(file_path: str) -> Dict[str, object] | None:
    """
    Read a yaml file from disk
    """
    try:
        with open(file_path, encoding='utf8') as file:
            data = yaml.safe_load(file)
            file.close()
        logging.debug(f"Yaml file: {file_path} loaded")
        return data

    except Exception as message:
        logging.error(f"Impossible to load the file: {file_path}")
        logging.error(f"Error: {message}")
        return None
