import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

#token
OJAMA_TOKEN = os.getenv("TOKEN_OJAMA")

#role
DUELIT_ID = os.getenv("DUELIST_ID")
TEAM_ID = os.getenv("TEAM_ID")