from nextcord.ext import commands
from gtts import gTTS
from views.admin.speakModal import SpeakModal
from nextcord import slash_command

import config

class Admin(commands.Cog):
    """Admin cmd"""
    def __init__(self,bot):
        self.bot = bot

    
    @commands.is_owner()
    @commands.command()
    async def test(self,ctx : commands.Context):
        chn = ctx.channel
        test = await chn.tgger_rityping()
      
    @slash_command(description="🎙️",dm_permission=False,default_member_permissions= 0)
    async def speak(self, interaction, message : str = None):
        """Send a message in a channel"""
        if message :
            try:
                await interaction.channel.send(message)
                await interaction.response.send_message("Message sent !",ephemeral=True)
            except Exception as e:          
                await interaction.response.send_message(f"Error : {e}",ephemeral=True)
        else :
            await interaction.response.send_modal(SpeakModal(self.bot,interaction.channel.id))

    @commands.has_role(int(config.BOT_DEV_ID))
    @commands.command()
    async def mp(self,ctx : commands.Context, player_id, *msg : str):
        """Send a message in dm"""

        guild = self.bot.get_guild(int(config.GUILD_ID))
        member = await guild.fetch_member(player_id)
        dm = await member.create_dm()
        message = ' '.join( msg)
        await dm.send(message)
          
    @commands.has_role(int(config.BOT_DEV_ID))
    @commands.command("tts_admin")
    async def  speak_tts(self,ctx : commands.Context, channel_id :int, *msg : str):
        """Send a vocal message in a channel"""

        voice_channel = self.bot.get_channel(channel_id)
        message = ' '.join( msg)
        voice = gTTS(text=message, lang='fr',slow=False)
        voice.save("audios/tts.mp3")

        await self.bot.play_sound("tts.mp3",voice_channel)
      
        
def setup(bot):
    bot.add_cog(Admin(bot))
