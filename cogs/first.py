import asyncio
import datetime as dt
import random

import discord
from discord.ext import commands

from .utils import views as u

class Scraping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['d'])
    async def dico(self, ctx, *arg):
        await ctx.channel.send("Je feuillette mon dico...")
        msg = await u.lookup(arg)
        await ctx.channel.send(msg)

    @commands.command()
    async def appel(self, ctx):
        await ctx.channel.send("Une seconde, j'allume mon minitel...")
        msgs = await u.callForText()

        for msg in msgs:
            await ctx.channel.send(msg)

    @commands.command(aliases=['r'])
    async def rare(self, ctx):
        await ctx.channel.send("QUE LA CULTURE COMMENCE")
        a_day = 86400
        mots_rares = ["Badigeon", "Diamanter", "sotie", "adipeux", "Pignon", "antienne",
            "Scient", "Survoûter", "Matutinal", "sidéral", "Sempiternel", "méandreux", "Sinapisé",
            "Sidération", "ancillaire", "épure", "inclémence", "infatué", "circonlocutions",
            "falot", "maritorne", "haridelle", "venelle", "émerillonné", "désespérance", "rudéral",
            "pleurard", "furfuracé", "grège", "fantomal", "galetas", "vaguer", "piriforme",
            "marcescent", "pulvérulent", "mascaret", "fondrière", "accore", "aventurine",
            "amarante", "pendeloque", "remembrance", "ocellé", "niellé", "obturer",
            "pétrichor", "coruscant"
        ]

        while True:
            random_word = random.choice(mots_rares)
            msg = await u.lookup(random_word)
            await ctx.channel.send("Le mot du jour est...")
            await ctx.channel.send(msg)
            await asyncio.sleep(a_day)

    @commands.command(aliases=['grou'])
    async def gro(self, ctx):
        await ctx.channel.send("QUE LA CULTURE COMMENCE")
        await ctx.channel.send(await u.rare_word())

async def setup(bot): # set async function
    await bot.add_cog(Scraping(bot)) # Use await