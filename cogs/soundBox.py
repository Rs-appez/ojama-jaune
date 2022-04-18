from nextcord.ext import commands


class SoundBox(commands.Cog):
    """Manage cardmarket commands"""
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def baobaboon(self, ctx):
        await ctx.send("https://beyondtheduel.com/wp-content/uploads/2017/01/MACR-Baobaboon-Feature.jpg")
        voice = ctx.message.author.voice
        if(voice): 
         voice_channel = voice.channel
         await self.bot.play_sound("baobaboon.wav",voice_channel)

    @commands.command()
    async def orelsan(self, ctx):
        voice = ctx.message.author.voice
        if(voice): 
         voice_channel = voice.channel
         await self.bot.play_sound("orelsan.m4a",voice_channel)
def setup(bot):
    bot.add_cog(SoundBox(bot))