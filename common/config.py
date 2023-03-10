import os
from dotenv import load_dotenv


def load_config(path: str) -> dict:
    """
    config loader from env file
    """
    load_dotenv(path)
    return {
        'port': os.getenv('API_PORT'),
        'host': os.getenv('API_HOST'),
        'debug': os.getenv('DEBUG'),
    }
