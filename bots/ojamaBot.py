import asyncio
import nextcord
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio,Message,ChannelType
from config import BOT_TEST_CHANNEL, GUILD_APPEZ_ID, GUILD_ID , CLOWN_ID ,CANARD_ID,LOUP_ID,NINJA_ID,BAOBABOON_ID,SINGE_ID

class OjamaBot(commands.Bot):

    def __init__(self, command_prefix ,production):

        self.voice_client = None
        self.production = production
        intents = nextcord.Intents.default()
        intents.members = True
        intents.voice_states = True
        intents.message_content = True
        self.oj_emoji = None
        self.game_emojis = {}

        super().__init__(command_prefix, intents=intents)

    async def on_voice_state_update(self,member,before,after):

        if (after.channel and not before.channel) or (before.self_mute and not after.self_mute) :
            if any(role.id == int(CLOWN_ID) for role in member.roles):
                await self.play_sound("circus.m4a",after.channel)
            
            elif any(role.id == int(CANARD_ID) for role in member.roles):
                await self.play_sound("bruit-de-canard-pour-montage.m4a",after.channel)

            elif any(role.id == int(LOUP_ID) for role in member.roles):
                await self.play_sound("loup.m4a",after.channel)

            elif any(role.id == int(NINJA_ID) for role in member.roles):
                await self.play_sound("ninja.mp3",after.channel)

            elif any(role.id == int(BAOBABOON_ID) for role in member.roles):
                await self.play_sound("baobaboon.wav",after.channel)

            elif any(role.id == int(SINGE_ID) for role in member.roles):
                await self.play_sound("baton magique.m4a",after.channel)

    async def on_ready(self):
        print(f"{self.user.display_name} est pret")
        guild = self.get_guild(int(GUILD_ID))
        if guild :
            self.oj_emoji= await guild.fetch_emoji(1027165609278050355)
            msg = await guild.get_channel(int(BOT_TEST_CHANNEL)).send("UP !")
            await msg.add_reaction(self.oj_emoji)
        await self.__get_game_emoji()

    async def __get_game_emoji(self):
        guild = self.get_guild(int(GUILD_APPEZ_ID))
        if guild :
            self.game_emojis["monster"] = await guild.fetch_emoji(1102722303936176178)
            self.game_emojis["spell"] = await guild.fetch_emoji(1102733166923497572)
            self.game_emojis["trap"] = await guild.fetch_emoji(1102733194819809400)

    async def on_message(self,message : Message):

        if message.author == self.user:
            return

        if message.content.startswith(self.command_prefix):
            await self.process_commands(message)

        elif message.channel.type == ChannelType.private:

            guild = self.get_guild(int(GUILD_ID))
            if guild :
                await guild.get_channel(int(BOT_TEST_CHANNEL)).send(f"{message.author} mp me : \n{message.content}")
                    

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

        if self.production :
            source =  FFmpegPCMAudio(source = f'audios/{sound}')
        else :
            source =  FFmpegPCMAudio( source = f'audios/{sound}',executable='ffmpeg\\ffmpeg.exe')
        
        self.voice_client = await self.join_vocal(voice_channel)

        self.voice_client.play(source, after= self.after_sound )
        
    
