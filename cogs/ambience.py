from discord import Member
from nextcord.ext import commands


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
        await dm_chan.send("hello")

    @commands.command()
    async def ojama(self,ctx):
        await ctx.send("JAUNE !!!!!!!!!!!!!!!!!") 
        await ctx.send("https://tenor.com/view/yu-gi-oh-gx-ojama-anime-monster-gif-17847003") 

        
    @commands.command()
    async def ojamaSucks(self,ctx):
        await ctx.author.edit(nick="ojama slave" )

        
def setup(bot):
    bot.add_cog(Ambiance(bot))