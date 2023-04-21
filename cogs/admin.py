from nextcord.ext import commands
from gtts import gTTS

from config import GUILD_ID,BOT_DEV_ID

class Admin(commands.Cog):
    """Admin cmd"""
    def __init__(self,bot):
        self.bot = bot

    
    @commands.is_owner()
    @commands.command()
    async def test(self,ctx : commands.Context):
        chn = ctx.channel
        test = await chn.tgger_rityping()
      
    @commands.has_role(int(BOT_DEV_ID))
    @commands.command()
    async def speak(self,ctx : commands.Context, channel :int, *msg : str):

        text_channel = self.bot.get_channel(channel)
        message = ' '.join( msg)
        await text_channel.send(message)

    @commands.has_role(int(BOT_DEV_ID))
    @commands.command()
    async def mp(self,ctx : commands.Context, player, *msg : str):

        guild = self.bot.get_guild(int(GUILD_ID))
        member = await guild.fetch_member(player)
        dm = await member.create_dm()
        message = ' '.join( msg)
        await dm.send(message)
          
    @commands.has_role(int(BOT_DEV_ID))
    @commands.command("tts_admin")
    async def  speak_tts(self,ctx : commands.Context, channel :int, *msg : str):

        voice_channel = self.bot.get_channel(channel)
        message = ' '.join( msg)
        voice = gTTS(text=message, lang='fr',slow=False)
        voice.save("audios/tts.mp3")

        await self.bot.play_sound("tts.mp3",voice_channel)
      
        
def setup(bot):
    bot.add_cog(Admin(bot))
