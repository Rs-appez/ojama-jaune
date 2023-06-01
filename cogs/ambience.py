import asyncio
from nextcord import Member
from nextcord import slash_command
from nextcord.ext import commands
import random

class Ambiance(commands.Cog):
    """Manage ambience with ojama"""
    def __init__(self,bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot:
            return

        if self.bot.oj_emoji:
            if 'ojama' in message.content.lower():
                await message.add_reaction(self.bot.oj_emoji)


    @commands.command()
    async def hello(self,ctx):
        member = ctx.author
        await ctx.send(f'hello {member.mention}')

    @slash_command()
    async def ninja(self,interaction):
        await interaction.response.send_message("https://cdn.discordapp.com/attachments/932758310187323406/965365644663074856/260149168_195516529440233_5949446936699436585_n.png")


    @commands.command()
    async def ojama(self,ctx):
        await ctx.send("JAUNE !!!!!!!!!!!!!!!!!") 
        await ctx.send("https://tenor.com/view/yu-gi-oh-gx-ojama-anime-monster-gif-17847003") 

    
    @commands.command(name="blague")
    async def joke(self, ctx):
        """Ask me my best joke"""

        await ctx.send("Quel est le comble pour un joueur branded")
        await asyncio.sleep(5)
        await ctx.send("de marquer ses cartes")
        
        
    @commands.command(name="tg")
    async def tg(self, ctx, mention : Member):
        nbr = random.randrange(1, 100, 1)
        user = ctx.guild.get_member_named(str(mention))
        assert isinstance(user, Member)
        if nbr <= 50:
            await ctx.author.edit(voice_channel=None)
        else:
            await user.edit(voice_channel=None)
        
    
        
def setup(bot):
    bot.add_cog(Ambiance(bot))