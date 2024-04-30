import os
import bots.ojamaBot as ojamaBot
import config

from interaction_discord_bot.init_cog import init_cog

debug = config.DEBUG

if debug :
    cmd_prefix = "§"
else :
    cmd_prefix = "!"


ojama_jaune = ojamaBot.OjamaBot(cmd_prefix)

for file in os.listdir("./cogs"):
    if(file.endswith(".py")):
        ojama_jaune.load_extension(f"cogs.{file[:-3]}")

init_cog(ojama_jaune)

ojama_jaune.run(config.OJAMA_JAUNE_TOKEN)