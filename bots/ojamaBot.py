import asyncio
from discord import PCMVolumeTransformer
import nextcord
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio

from io import BufferedIOBase
class OjamaBot(commands.Bot):

    def __init__(self):
        intents = nextcord.Intents.default()
        intents.members = True
        intents.voice_states = True
        super().__init__(command_prefix = "!", intents=intents)


    async def on_ready(self):
        print(f"{self.user.display_name} est pret")

    async def join_vocal(self, voice_channel : nextcord.VoiceChannel):

        voice = await voice_channel.connect()
        source =  FFmpegPCMAudio(executable='ffmpeg\\ffmpeg.exe', source = 'audios\\baobaboon.wav')
        assert isinstance(source,FFmpegPCMAudio)
        voice.play(source)
        await asyncio.sleep(1)
        await self.left_vocal(voice)

    async def left_vocal(self, voice_client : nextcord.VoiceClient):

        await voice_client.disconnect()
    
