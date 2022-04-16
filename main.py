
import os
import bots.ojamaBot as ojamaBot
import config

ojama_jaune = ojamaBot.OjamaBot()

for file in os.listdir("./cogs"):
    if(file.endswith(".py")):
        ojama_jaune.load_extension(f"cogs.{file[:-3]}")

ojama_jaune.run(config.OJAMA_TOKEN)