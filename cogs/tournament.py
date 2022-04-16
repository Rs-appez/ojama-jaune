from nextcord.ext import commands
import time
from models.timer import Timer
 

class Tournament(commands.Cog):
    """Manage yugioh tournament"""
    def __init__(self,bot):
        self.bot = bot
        self.timer = Timer(10)

    async def launch_timer(self, ctx):
        await ctx.send(5)
        for i in range(5):           
            async for message in ctx.message.channel.history(limit = 1):
                time.sleep(1)
                if(i != 4):
                    await message.edit(content=4-i)
                else:
                     await message.edit(content="TIME TO DUEL")
        self.timer.start()

        await ctx.send("TIME !!!!!!!!!!!!!!")

    @commands.command()
    async def timer(self,ctx):
        """Timer for a duel"""

        await self.launch_timer(ctx)
      


        
def setup(bot):
    bot.add_cog(Tournament(bot))