import asyncio
import nextcord
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio,Message,ChannelType
from config import BOT_TEST_CHANNEL, GUILD_APPEZ_ID, GUILD_ID , CLOWN_ID ,CANARD_ID,LOUP_ID,NINJA_ID,BAOBABOON_ID,SINGE_ID,GUILD_APPEZ_CELLAR_ID

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
        guild_cellar = self.get_guild(int(GUILD_APPEZ_CELLAR_ID))

        if guild :
            #type card
            self.game_emojis["monster"] = await guild.fetch_emoji(1102722303936176178)
            self.game_emojis["spell"] = await guild.fetch_emoji(1102733166923497572)
            self.game_emojis["trap"] = await guild.fetch_emoji(1102733194819809400)
            #type spell/card
            self.game_emojis["continuous"] = await guild.fetch_emoji(1102754344698384505)
            self.game_emojis["counter"] = await guild.fetch_emoji(1102754346220912710)
            self.game_emojis["equip"] = await guild.fetch_emoji(1102754351254089820)
            self.game_emojis["field"] = await guild.fetch_emoji(1102754352692744323)
            self.game_emojis["normal"] = await guild.fetch_emoji(1102754356287254628)
            self.game_emojis["quick-play"] = await guild.fetch_emoji(1102754593294786601)
            self.game_emojis["ritual"] = await guild.fetch_emoji(1102754359462346823)
            #attribute
            self.game_emojis["dark"] = await guild.fetch_emoji(1102754347575681084)
            self.game_emojis["divine"] = await guild.fetch_emoji(1102754349702193172)
            self.game_emojis["fire"] = await guild.fetch_emoji(1102754588685254667)
            self.game_emojis["water"] = await guild.fetch_emoji(1102754596721541270)
            self.game_emojis["wind"] = await guild.fetch_emoji(1102754598227296316)
            self.game_emojis["light"] = await guild.fetch_emoji(1102754591549952000)
            self.game_emojis["earth"] = await guild.fetch_emoji(1102860006610702376)
            #type monster
            self.game_emojis["aqua"] = await guild.fetch_emoji(1102864888159809566)
            self.game_emojis["beast"] = await guild.fetch_emoji(1102864889447465070)
            self.game_emojis["beast-warrior"] = await guild.fetch_emoji(1102878729673396246)
            self.game_emojis["creator god"] = await guild.fetch_emoji(1102878731451764746)
            self.game_emojis["cyberse"] = await guild.fetch_emoji(1102878734165475368)
            self.game_emojis["dinosaur"] = await guild.fetch_emoji(1102878735474118686)
            self.game_emojis["divine-beast"] = await guild.fetch_emoji(1102878737822912542)
            self.game_emojis["dragon"] = await guild.fetch_emoji(1102878800829755443)
            self.game_emojis["fairy"] = await guild.fetch_emoji(1102878803275022336)
            self.game_emojis["fiend"] = await guild.fetch_emoji(1102878804705284167)
            self.game_emojis["fish"] = await guild.fetch_emoji(1102878806315900938)
            self.game_emojis["illusionist"] = await guild.fetch_emoji(1102878896900296716)
            self.game_emojis["insect"] = await guild.fetch_emoji(1102878808337555486)
            self.game_emojis["machine"] = await guild.fetch_emoji(1102878809784594463)
            self.game_emojis["plant"] = await guild.fetch_emoji(1102878845318746122)
            self.game_emojis["psychic"] = await guild.fetch_emoji(1102878847734644736)
            self.game_emojis["pyro"] = await guild.fetch_emoji(1102878849307529267)
            self.game_emojis["reptile"] = await guild.fetch_emoji(1102878850708426782)
            self.game_emojis["rock"] = await guild.fetch_emoji(1102878852969152572)
            self.game_emojis["sea serpent"] = await guild.fetch_emoji(1102878854210666537)
            self.game_emojis["spellcaster"] = await guild.fetch_emoji(1102878896900296716)
            self.game_emojis["thunder"] = await guild.fetch_emoji(1102878899223937024)
            self.game_emojis["warrior"] = await guild.fetch_emoji(1102878902210281552)
            self.game_emojis["winged beast"] = await guild.fetch_emoji(1102878904433246291)
            self.game_emojis["wyrm"] = await guild.fetch_emoji(1102878906245189704)
            self.game_emojis["zombie"] = await guild.fetch_emoji(1102878907725795349)
            #monster card type
            self.game_emojis["effect"] = await guild.fetch_emoji(1102722303936176178)
            self.game_emojis["tuner"] = await guild.fetch_emoji(1102722303936176178)
            self.game_emojis["normal "] = await guild.fetch_emoji(1102933726754770954)
            self.game_emojis["fusion"] = await guild.fetch_emoji(1102754338163654716)
            self.game_emojis["ritual "] = await guild.fetch_emoji(1102755626469298208)
            self.game_emojis["link"] = await guild.fetch_emoji(1102754339086401538)
            self.game_emojis["pendulum"] = await guild.fetch_emoji(1102934236702457917)
            self.game_emojis["synchro"] = await guild.fetch_emoji(1102754341313577020)
            self.game_emojis["xyz"] = await guild.fetch_emoji(1102754342626410627)
        if guild_cellar :
            #star level/rank
            self.game_emojis["level"] = await guild_cellar.fetch_emoji(1103435693130252428)
            self.game_emojis["rank"] = await guild_cellar.fetch_emoji(1103435695185473586)
        print("emo charged")

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
        
    
