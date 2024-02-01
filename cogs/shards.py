import asyncio
import datetime as dt
import random

import discord
from discord.ext import commands

from .utils.time_handler import *
from .utils.coureurs_texts import SprintEndText
from .utils.db import DBHandler
from cogs.utils import scrapers as scr


class Shards(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sprint = False
        self.runners = {}
        self.enders = {}

    @commands.command(aliases=["sh"])
    async def shards(self, ctx, *arg):
        is_player = await scr.ShardsGame.is_player(ctx.message.author.id)
        await ctx.channel.send(is_player)

async def setup(bot): # set async function
    await bot.add_cog(Shards(bot)) # Use await