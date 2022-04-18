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
        
    @commands.command()
    async def baobaboon(self, ctx):
        await ctx.send("https://www.google.com/url?sa=i&url=https%3A%2F%2Fdb.ygoprodeck.com%2Fcard%2F%3Fsearch%3DBaobaboon&psig=AOvVaw38GKreKmNu415uta-7DAJQ&ust=1650321878244000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCPDO56GWnPcCFQAAAAAdAAAAABAR")
        
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