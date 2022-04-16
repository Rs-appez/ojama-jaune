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
    async def mp    (self,ctx):
        member : Member =  ctx.author
        dm_chan = await member.create_dm()
        await dm_chan.send("hello")

    @commands.command()
    async def ojama(self,ctx):
        await ctx.send("JAUNE !!!!!!!!!!!!") 

        
def setup(bot):
    bot.add_cog(Ambiance(bot))