from nextcord.ext import commands
from nextcord import slash_command
from gtts import gTTS
from nextcord.interactions import Interaction

from nextcord import InteractionContextType


class SoundBox(commands.Cog):
    """Manage cardmarket commands"""

    def __init__(self, bot):
        self.bot: commands.Bot = bot

    async def play_sound(self, author, voice, sound):

        voice_channel = None

        if not voice:
            voice = author.voice
            if voice:
                voice_channel = voice.channel
        else:
            # voice_channel = ctx.guild.get_channel(voice)
            voice_channel = self.bot.get_channel(voice)

        if voice_channel:

            await self.bot.play_sound(sound, voice_channel)

    def tts(self, msg, lan="fr"):
        voice = gTTS(text=msg, lang=lan, slow=False)
        voice.save("audios/tts.mp3")

    @slash_command(
        name="baobaboon", description="THE CALL OF BAOBABOON", contexts=[InteractionContextType.guild]
    )
    async def baobaboon(self, interaction: Interaction):

        await self.play_sound(interaction.user, None, "baobaboon.wav")
        await interaction.response.send_message(
            "https://beyondtheduel.com/wp-content/uploads/2017/01/MACR-Baobaboon-Feature.jpg"
        )

    @slash_command(name="blue", description="Da Ba Dee", contexts=[InteractionContextType.guild])
    async def blue(self, interaction: Interaction):

        await self.play_sound(interaction.user, None, "bluedabedi.m4a")
        await interaction.response.send_message(
            "https://tenor.com/view/yass-slayy-blue-subway-gif-26002963"
        )

    @slash_command(name="delu", description="le deni", contexts=[InteractionContextType.guild])
    async def desillusion(self, interaction: Interaction, target):

        await self.play_sound(interaction.user, None, "delu.m4a")
        await interaction.response.send_message(f"{target} est dans le denis")

    @slash_command(name="cdlamerde", description="'-'", contexts=[InteractionContextType.guild])
    async def karadoc(self, interaction: Interaction):

        await self.play_sound(interaction.user, None, "c dlamerde.m4a")
        await interaction.response.send_message(
            content="https://tenor.com/view/karadoc-kaamelott-gif-18243163"
        )

    @slash_command(
        name="dimitri_shōkan", description="⚠ DANGER ⚠ ", contexts=[InteractionContextType.guild]
    )
    async def fdp(self, interaction: Interaction):

        await self.play_sound(interaction.user, None, "FDP.mp3")
        await interaction.response.send_message(
            content="https://media.discordapp.net/attachments/964951777273339914/1069104836177580062/fdp.png?width=1039&height=528"
        )

    @slash_command(name="gogole", description="⚠ ALERTE ⚠ ", contexts=[InteractionContextType.guild])
    async def gogole(self, interaction: Interaction):

        await self.play_sound(interaction.user, None, "gogole.mp3")
        await interaction.response.send_message(
            content="https://tenor.com/view/lol-crazy-alerte-garrison-south-park-gif-14631935"
        )

    @slash_command(name="jmbun", description="J'AIME BIEN !", contexts=[InteractionContextType.guild])
    async def jmbun(self, interaction: Interaction):

        await self.play_sound(interaction.user, None, "jaimebun.m4a")

        if interaction.user.nick:
            name = interaction.user.nick
        else:
            name = interaction.user.name

        await interaction.response.send_message(content=f"{name} a bien aimé !")

    @slash_command(name="feur", description="☣ NE PAS UTILISER ☣", contexts=[InteractionContextType.guild])
    async def feur(self, interaction: Interaction):

        await self.play_sound(interaction.user, None, "FEUR.wav")
        await interaction.response.send_message(
            content="https://media.discordapp.net/attachments/964951777273339914/1069105361035993278/IMG_20220416_205138_438.jpg?width=1173&height=528"
        )

    @slash_command(name="emotional_damage", description="AIE", contexts=[InteractionContextType.guild])
    async def emotional(self, interaction: Interaction):

        await self.play_sound(interaction.user, None, "emotional-damage.mp3")
        await interaction.response.send_message(
            content="https://tenor.com/view/emotional-damage-meme-gif-25259043"
        )

    @slash_command(name="paka", description="NICAIZIZ", contexts=[InteractionContextType.guild])
    async def maxime(self, interaction: Interaction):

        await self.play_sound(interaction.user, None, "maxime.mp3")
        await interaction.response.send_message(content="aka nicolas")

    @slash_command(
        name="baton_magique", description="TUN TUN TUN TINTIN", contexts=[InteractionContextType.guild]
    )
    async def baton_magique(self, interaction: Interaction):

        await self.play_sound(interaction.user, None, "baton magique.m4a")
        await interaction.response.send_message(
            content="https://tenor.com/view/goku-gif-26185626"
        )

    @slash_command(name="tts", description="Text to speak", contexts=[InteractionContextType.guild])
    async def speak_tts(self, interaction: Interaction, msg: str, lang: str = "fr"):
        self.tts(msg, lang)
        await self.play_sound(interaction.user, None, "tts.mp3")
        if self.bot.oj_emoji:
            await interaction.response.send_message(
                content=f"{self.bot.oj_emoji} J'ai dit ton message {self.bot.oj_emoji}",
                ephemeral=True,
            )
        else:
            await interaction.response.send_message(
                ":upside_down: J'ai dit ton message :upside_down: ", ephemeral=True
            )


def setup(bot):
    bot.add_cog(SoundBox(bot))
