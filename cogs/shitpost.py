import discord
from discord.ext import commands

from .utils.shitpost import *
from .utils.resources import gojo, laments, sensim


class Shitpost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["d", "D"])
    async def drama(self, ctx):
        await ctx.send("https://tenor.com/view/dramatic-chipmunk-gif-19778021")

    @commands.command(aliases=['g', 'G'])
    async def gojo(self, ctx):
        user = ctx.message.author
        await user.send(random.choice(gojo))

    @commands.command(aliases=['o', 'O'])
    async def ouin(self, ctx):
        await ctx.send(random.choice(laments))

    @commands.command(aliases=['q', 'Q', 'cielly'])
    async def queenie(self, ctx, *, message=None):
        if message == None:
            message = "Certes, mais que dois-je quueener ?"
        else:
            message = f"Ainsi parla Queenie : {queenize(message)}"
        await ctx.send(message)

    @commands.command()
    async def sen(self, ctx):
        await ctx.send(random.choice(sensim))

    @commands.command()
    async def sne(self, ctx):
        await ctx.send(queenize(random.choice(sensim)))


async def setup(bot): # set async function
    await bot.add_cog(Shitpost(bot)) # Use await