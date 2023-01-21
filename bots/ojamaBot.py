import asyncio
import nextcord
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio
from config import BOT_TEST_CHANNEL, GUILD_ID

class OjamaBot(commands.Bot):

    def __init__(self, command_prefix ):

        self.voice_client = None

        intents = nextcord.Intents.default()
        intents.members = True
        intents.voice_states = True
        super().__init__(command_prefix, intents=intents)


    async def on_ready(self):
        print(f"{self.user.display_name} est pret")
        guild = self.get_guild(int(GUILD_ID))
        if guild :
            msg = await guild.get_channel(int(BOT_TEST_CHANNEL)).send("UP !")
            emoji =  msg.guild.emojis[0]
            await msg.add_reaction(emoji)

    async def join_vocal(self, voice_channel : nextcord.VoiceChannel):

        return await voice_channel.connect()
        

    async def left_vocal(self):
        if(self.voice_client):
            await self.voice_client.disconnect()

    def after_sound(self,error):
        try:
            lv = self.left_vocal()
            fut = asyncio.run_coroutine_threadsafe(lv, self.loop)
            fut.result()
        except Exception as e:
            print(e)

    async def play_sound(self, sound : str, voice_channel : nextcord.VoiceChannel):

        self.voice_client = await self.join_vocal(voice_channel)
        source =  FFmpegPCMAudio( source = f'audios/{sound}')
        self.voice_client.play(source, after= self.after_sound )
        
    
