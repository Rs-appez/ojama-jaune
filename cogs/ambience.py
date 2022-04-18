import asyncio
from discord import Member
from nextcord.ext import commands

from config import JUSTIN_ID

class Ambiance(commands.Cog):
    """Manage ambience with ojama"""
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def hello(self,ctx):
        member = ctx.author
        await ctx.send(f'hello {member.mention}')

    @commands.command()
    async def mp (self,ctx):
        member : Member =  ctx.author
        dm_chan = await member.create_dm()
        await dm_chan.send("https://static.wikia.nocookie.net/yugioh-gx/images/3/38/Ojama_Delta_Combin%C3%A9.png/revision/latest?cb=20140311110956&path-prefix=fr")

    @commands.command()
    async def ojama(self,ctx):
        await ctx.send("JAUNE !!!!!!!!!!!!!!!!!") 
        await ctx.send("https://tenor.com/view/yu-gi-oh-gx-ojama-anime-monster-gif-17847003") 

    @commands.command()
    async def emotional(self, ctx):
        await ctx.send("https://tenor.com/view/emotional-damage-emotional-damage-meme-funny-gif-24332819")
        
    @commands.command(name="blague")
    async def joke(self, ctx):
        await ctx.send("Quel est le comble pour un joueur branded")
        await asyncio.sleep(5)
        await ctx.send("de marquer ses cartes")
        
   
        
    @commands.command()
    async def ojamaSucks(self,ctx):
        await ctx.author.edit(nick="ojama slave" )


    @commands.command()
    async def tgjustin(self, ctx : commands.Context):

        async for msg in ctx.channel.history(limit=1):
            await msg.delete()
        
        user = ctx.guild.get_member(JUSTIN_ID)
        await user.edit(voice_channel=None)
        await ctx.author.edit(voice_channel=None)
        
        
def setup(bot):
    bot.add_cog(Ambiance(bot))