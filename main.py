import os
import bots.ojamaBot as ojamaBot
import config
from serv import keep_alive
#------------BOT PROD--------------------------

ojama_jaune = ojamaBot.OjamaBot("!")

for file in os.listdir("./cogs"):
    if(file.endswith(".py")):
        ojama_jaune.load_extension(f"cogs.{file[:-3]}")

keep_alive()
ojama_jaune.run(config.OJAMA_JAUNE_TOKEN)