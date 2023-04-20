import asyncio
import datetime as dt
import random

import discord
from discord.ext import commands

from .utils.coureur import *

class Coureur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['r'])
    async def rhah(self, ctx, *arg):
        error = """
        Merci de formater votre message de la façon suivante :
        ```course à 15 pour 30``` (unités en minutes)
        """        
        sprint = calculate_sprint(arg)

        if sprint == False:
            await ctx.channel.send(error)
        else:
            await ctx.channel.send(sprint)

async def setup(bot): # set async function
    await bot.add_cog(Coureur(bot)) # Use await