from nextcord.ext import commands


class SoundBox(commands.Cog):
    """Manage cardmarket commands"""
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def baobaboon(self, ctx):
        await ctx.send("https://beyondtheduel.com/wp-content/uploads/2017/01/MACR-Baobaboon-Feature.jpg")
        await self.bot.play_sound("baobaboon",ctx.message.author.voice.channel)
def setup(bot):
    bot.add_cog(SoundBox(bot))