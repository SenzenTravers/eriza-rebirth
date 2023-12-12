import asyncio
import datetime as dt
import random

import discord
from discord.ext import commands

class Coureur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["x"])
    async def bleh(self, ctx, *arg):
        server_id = ctx.message.guild.id