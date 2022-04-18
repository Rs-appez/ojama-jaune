import discord
from nextcord.ext import commands



class OjamaBot(commands.Bot):

    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(command_prefix = "!", intents=intents)


    async def on_ready(self):
        print(f"{self.user.display_name} est pret")
    
