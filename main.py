import os
import bots.ojamaBot as ojamaBot
import config

debug = config.DEBUG

if debug :
    cmd_prefix = "§"
else :
    cmd_prefix = "!"


ojama_jaune = ojamaBot.OjamaBot(cmd_prefix,not debug)

for file in os.listdir("./cogs"):
    if(file.endswith(".py")):
        ojama_jaune.load_extension(f"cogs.{file[:-3]}")

ojama_jaune.run(config.OJAMA_JAUNE_TOKEN)