import asyncio
import datetime as dt
import random

import discord
from discord.ext import commands

from .utils import scrapers

class Productivity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['na'])
    async def new_appels(self, ctx):
        """
        Commande admin ? Ou, plutôt, le bot devrait-il poster automatiquement
        les nouvelles ?
        """
        # channel = self.bot.get_channel(1100150577708662824)
        #TODO : regex, alas, and compare regex
        channel = self.bot.get_channel(1100150577708662824)

        get_all_contests = await scrapers.WritingContest.format_contests(by_added=True)
        get_all_contests = get_all_contests[:10]
        most_recent_posted = []

        async for message in channel.history(limit=10):
            most_recent_posted.append(message.content)

        to_post = set(get_all_contests).difference(most_recent_posted)
        to_post = [con for con in get_all_contests if con not in most_recent_posted]
        to_post.reverse()

        for contest in to_post:
            await channel.send(contest)

    @commands.command(aliases=['a'])
    async def appels(self, ctx):
        """
        Envoie par MP les appels à texte classés par deadline
        """
        await ctx.channel.send("Une seconde, j'allume mon minitel...")
        async with ctx.channel.typing():
            contests = await scrapers.WritingContest.format_contests(
                by_added=False, by_deadline=True)

            contests.reverse()

            for contest in contests:
                user = ctx.message.author
                await user.send(contest)

    # @commands.command(aliases=['r'])
    # async def rare(self, ctx):
    #     await ctx.channel.send("QUE LA CULTURE COMMENCE")
    #     a_day = 86400
    #     mots_rares = ["Badigeon", "Diamanter", "sotie", "adipeux", "Pignon", "antienne",
    #         "Scient", "Survoûter", "Matutinal", "sidéral", "Sempiternel", "méandreux", "Sinapisé",
    #         "Sidération", "ancillaire", "épure", "inclémence", "infatué", "circonlocutions",
    #         "falot", "maritorne", "haridelle", "venelle", "émerillonné", "désespérance", "rudéral",
    #         "pleurard", "furfuracé", "grège", "fantomal", "galetas", "vaguer", "piriforme",
    #         "marcescent", "pulvérulent", "mascaret", "fondrière", "accore", "aventurine",
    #         "amarante", "pendeloque", "remembrance", "ocellé", "niellé", "obturer",
    #         "pétrichor", "coruscant"
    #     ]

    #     while True:
    #         random_word = random.choice(mots_rares)
    #         msg = await u.lookup(random_word)
    #         await ctx.channel.send("Le mot du jour est...")
    #         await ctx.channel.send(msg)
    #         await asyncio.sleep(a_day)

    # @commands.command(aliases=['grou'])
    # async def gro(self, ctx):
    #     await ctx.channel.send("QUE LA CULTURE COMMENCE")
    #     await ctx.channel.send(await u.rare_word())

async def setup(bot):
    await bot.add_cog(Productivity(bot))