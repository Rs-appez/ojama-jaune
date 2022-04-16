import os
from dotenv import load_dotenv
import bots.ojamaBot as ojamaBot

load_dotenv(dotenv_path="config")

ojama_jaune = ojamaBot.OjamaBot()

for file in os.listdir("./cogs"):
    if(file.endswith(".py")):
        ojama_jaune.load_extension(f"cogs.{file[:-3]}")

ojama_jaune.run(os.getenv("TOKEN_OJAMA"))