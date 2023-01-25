from discord import VoiceChannel
import nextcord
from nextcord.ext import commands
from nextcord import slash_command
from gtts import gTTS


class SoundBox(commands.Cog):
    """Manage cardmarket commands"""
    def __init__(self,bot):
        self.bot : commands.Bot = bot

    async def play_sound(self, ctx, voice,sound):

        voice_channel = None

        if(not voice):
            voice = ctx.message.author.voice
            if(voice): 
                voice_channel = voice.channel
        else :
            # voice_channel = ctx.guild.get_channel(voice)
            voice_channel = self.bot.get_channel(voice)

        if(voice_channel):

            await self.bot.play_sound(sound,voice_channel)

    def tts (self, msg, lang='fr'):
        voice = gTTS(text=msg, lang='fr',slow=False)
        voice.save("audios/tts.mp3")


    @commands.command()
    async def baobaboon(self, ctx : commands.Context, voice : int = None):
        await ctx.send("https://beyondtheduel.com/wp-content/uploads/2017/01/MACR-Baobaboon-Feature.jpg")
        
        await self. play_sound(ctx, voice,"baobaboon.wav")

    @commands.command()
    async def orelsan(self, ctx, voice : int = None):

        await self. play_sound(ctx, voice,"orelsan.m4a")

    @commands.command()
    async def fdp(self, ctx, voice : int = None):

        await self. play_sound(ctx, voice,"FDP.mp3")
        await ctx.send(file=nextcord.File("images/fdp.png"))

    @commands.command()
    async def gogole(self, ctx, voice : int = None):
        await self. play_sound(ctx, voice,"gogole.mp3")

    @commands.command()
    async def jmbun(self, ctx, voice : int = None):
        await self. play_sound(ctx, voice,"jaimebun.m4a")

    @commands.command()
    async def feur(self, ctx, voice : int = None):

        await self. play_sound(ctx, voice,"FEUR.wav")
        await ctx.send(file=nextcord.File("images/IMG_20220416_205138_438.jpg"))

    @commands.command()
    async def emotional(self, ctx, voice : int = None):
        await self. play_sound(ctx, voice,"emotional-damage.mp3")

    @commands.command(name="paka")
    async def maxime(self, ctx, voice : int = None):
        await self. play_sound(ctx, voice,"maxime.mp3")

    @commands.command(name="bm")
    async def baton_magique(self, ctx, voice : int = None):
        await self. play_sound(ctx, voice,"baton magique.m4a")
    
    @slash_command(name='tts',description='Text to speak')
    async def speak_tts(self,ctx : commands.Context, lang : str = 'fr', *msg : str):
        message = ' '.join(msg)
        self.tts(message, lang)
        async for msg in ctx.channel.history(limit=1):
             await msg.delete()
            
        await self. play_sound(ctx, None,"tts.mp3")


    @commands.command()
    async def jujujustin(self, ctx):
        member = ctx.guild.get_member(377207249937891329)
        self.tts('Ju Ju Just1 4 !')
        await self. play_sound(ctx, None,"tts.mp3")
        await ctx.send(f'Ju Ju {member.mention} !')
        await ctx.send("https://media.discordapp.net/attachments/696053977070043247/1064940462684786709/jujujustin.png")

def setup(bot):
    bot.add_cog(SoundBox(bot))