import os
import bots.ojamaBot as ojamaBot
import config

#------------BOT DEV--------------------------

ojama_rouge = ojamaBot.OjamaBot("§")

for file in os.listdir("./cogs"):
    if(file.endswith(".py")):
        ojama_rouge.load_extension(f"cogs.{file[:-3]}")

ojama_rouge.run(config.OJAMA_ROUGE_TOKEN)