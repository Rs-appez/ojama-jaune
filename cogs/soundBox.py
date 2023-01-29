import nextcord
from nextcord.ext import commands
from nextcord import slash_command
from gtts import gTTS
from nextcord.interactions import Interaction


class SoundBox(commands.Cog):
    """Manage cardmarket commands"""
    def __init__(self,bot):
        self.bot : commands.Bot = bot

    async def play_sound(self, author, voice,sound):

        voice_channel = None

        if(not voice):
            voice = author.voice
            if(voice): 
                voice_channel = voice.channel
        else :
            # voice_channel = ctx.guild.get_channel(voice)
            voice_channel = self.bot.get_channel(voice)

        if(voice_channel):

            await self.bot.play_sound(sound,voice_channel)

    def tts (self, msg, lan='fr'):
        voice = gTTS(text=msg, lang=lan,slow=False)
        voice.save("audios/tts.mp3")


    @commands.command()
    async def baobaboon(self, ctx : commands.Context, voice : int = None):
        await ctx.send("https://beyondtheduel.com/wp-content/uploads/2017/01/MACR-Baobaboon-Feature.jpg")
        
        await self. play_sound(ctx.author, voice,"baobaboon.wav")

    @commands.command()
    async def orelsan(self, ctx, voice : int = None):

        await self. play_sound(ctx.author, voice,"orelsan.m4a")

    @commands.command()
    async def fdp(self, ctx, voice : int = None):

        await self. play_sound(ctx.author, voice,"FDP.mp3")
        await ctx.send(file=nextcord.File("images/fdp.png"))

    @commands.command()
    async def gogole(self, ctx, voice : int = None):
        await self. play_sound(ctx.author, voice,"gogole.mp3")

    @commands.command()
    async def jmbun(self, ctx, voice : int = None):
        await self. play_sound(ctx.author, voice,"jaimebun.m4a")

    @commands.command()
    async def feur(self, ctx, voice : int = None):

        await self. play_sound(ctx.author, voice,"FEUR.wav")
        await ctx.send(file=nextcord.File("images/IMG_20220416_205138_438.jpg"))

    @commands.command()
    async def emotional(self, ctx, voice : int = None):
        await self. play_sound(ctx.author, voice,"emotional-damage.mp3")

    @commands.command(name="paka")
    async def maxime(self, ctx, voice : int = None):
        await self. play_sound(ctx.author, voice,"maxime.mp3")

    @commands.command(name="bm")
    async def baton_magique(self, ctx, voice : int = None):
        await self. play_sound(ctx.author, voice,"baton magique.m4a")
    
    @slash_command(name='tts',description='Text to speak')
    async def speak_tts(self,interaction : Interaction, msg : str, lang : str = 'fr'):
        self.tts(msg, lang)
        await self. play_sound(interaction.user, None,"tts.mp3")
        emoji =  msg.guild.emojis[0]
        if emoji:
            await interaction.response.send_message(content=emoji+"J'ai dit ton message"+emoji,ephemeral=True)
        else :
            await interaction.response.send_message(":upside_down: J'ai dit ton message :upside_down: ",ephemeral=True)

    @commands.command()
    async def jujujustin(self, ctx):
        member = ctx.guild.get_member(377207249937891329)
        self.tts('Ju Ju Just1 4 !')
        await self. play_sound(ctx.author, None,"tts.mp3")
        if member:
            await ctx.send(f'Ju Ju {member.mention} !')
        await ctx.send("https://media.discordapp.net/attachments/696053977070043247/1064940462684786709/jujujustin.png")

def setup(bot):
    bot.add_cog(SoundBox(bot))