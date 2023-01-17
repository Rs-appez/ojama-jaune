import asyncio
from nextcord import Member
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

        if 'ojama' in message.content.lower():
            emoji =  message.guild.emojis[0]
            await message.add_reaction(emoji)


    @commands.command()
    async def hello(self,ctx):
        member = ctx.author
        await ctx.send(f'hello {member.mention}')

    @commands.command()
    async def ojama(self,ctx):
        await ctx.send("JAUNE !!!!!!!!!!!!!!!!!") 
        await ctx.send("https://tenor.com/view/yu-gi-oh-gx-ojama-anime-monster-gif-17847003") 

    @commands.command()
    async def jujujustin(self, ctx):
        member = ctx.guild.get_member(377207249937891329)
        await ctx.send(f'Ju Ju {member.mention} !')
        await ctx.send("https://media.discordapp.net/attachments/696053977070043247/1064940462684786709/jujujustin.png")
    
    @commands.command(name="blague")
    async def joke(self, ctx):
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