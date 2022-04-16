import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

OJAMA_TOKEN = os.getenv("TOKEN_OJAMA")