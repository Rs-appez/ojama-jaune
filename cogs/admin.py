from nextcord.ext import commands
from gtts import gTTS

class Admin(commands.Cog):
    """Admin cmd"""
    def __init__(self,bot):
        self.bot = bot

    
    @commands.is_owner()
    @commands.command()
    async def test(self,ctx : commands.Context):
        chn = ctx.channel
        test = await chn.tgger_rityping()
      
    
    @commands.is_owner()
    @commands.command()
    async def speak(self,ctx : commands.Context, channel :int, *msg : str):

        text_channel = self.bot.get_channel(channel)
        message = ' '.join( msg)
        await text_channel.send(message)
          
    @commands.is_owner()
    @commands.command("tts_admin")
    async def  speak_tts(self,ctx : commands.Context, channel :int, *msg : str):

        voice_channel = self.bot.get_channel(channel)
        message = ' '.join( msg)
        voice = gTTS(text=message, lang='fr',slow=False)
        voice.save("audios/tts.mp3")

        await self.bot.play_sound("tts.mp3",voice_channel)
      
        
def setup(bot):
    bot.add_cog(Admin(bot))