import nextcord
from nextcord.ext import commands


class SoundBox(commands.Cog):
    """Manage cardmarket commands"""
    def __init__(self,bot):
        self.bot : commands.Bot = bot

    @commands.command()
    async def baobaboon(self, ctx : commands.Context, voice : int = None):
        await ctx.send("https://beyondtheduel.com/wp-content/uploads/2017/01/MACR-Baobaboon-Feature.jpg")
        if(not voice):
            voice = ctx.message.author.voice
            if(voice): 
                voice_channel = voice.channel
        else :
            # voice_channel = ctx.guild.get_channel(voice)
            voice_channel = self.bot.get_channel(voice)
        
        if(voice_channel):
         await self.bot.play_sound("baobaboon.wav",voice_channel)

    @commands.command()
    async def orelsan(self, ctx):
        voice = ctx.message.author.voice
        if(voice): 
         voice_channel = voice.channel
         await self.bot.play_sound("orelsan.m4a",voice_channel)

    @commands.command()
    async def feur(self, ctx):
        voice = ctx.message.author.voice
        if(voice): 
         voice_channel = voice.channel
         await self.bot.play_sound("FEUR.wav",voice_channel)
         await ctx.send(file=nextcord.File("images\\IMG_20220416_205138_438.jpg"))


def setup(bot):
    bot.add_cog(SoundBox(bot))