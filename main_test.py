import os
import bots.ojamaBot as ojamaBot
from decouple import config

#------------BOT DEV--------------------------

ojama_rouge = ojamaBot.OjamaBot("§",False)

for file in os.listdir("./cogs"):
    if(file.endswith(".py")):
        ojama_rouge.load_extension(f"cogs.{file[:-3]}")

ojama_rouge.run(config('TOKEN_OJAMA_ROUGE'))