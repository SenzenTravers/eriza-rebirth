import asyncio
import datetime as dt
import random

import discord

from discord.ext import commands, tasks

from .utils import avis, db, scrapers
from .utils.time_handler import reminder_format

contest_time = dt.time(hour=19, minute=00)
word_time = dt.time(hour=12, minute=0)


class Productivity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.post_contests.start()
        self.random_mot.start()

    ############################# TÂCHES AUTOMATIQUES
    @tasks.loop(time=contest_time)
    async def post_contests(self):
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
            await asyncio.sleep(1)

    @tasks.loop(time=word_time)
    async def random_mot(self):
        chann = self.bot.get_channel(701536565947793569)
        db_obj = db.DBHandler()
        word = await db_obj.fetch_random_word()
        result = await scrapers.DictionaryThings.get_word(word[1])

        await chann.send(f"**LE MOT RARE DU JOUR**\n\n:book: {result}")

    ############################# COMMANDES
    @commands.command(aliases=['na'])
    async def new_appels(self, ctx):
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

    @commands.command()
    async def appels(self, ctx):
        """
        Envoie par MP les appels à texte classés par deadline
        """
        await ctx.channel.send("Une seconde, j'allume mon minitel...")
        async with ctx.channel.typing():
            contests = await scrapers.WritingContest.format_contests(
                by_added=False, by_deadline=True)

            contests.reverse()
            user = ctx.message.author

            for contest in contests:
                await user.send(contest)
                await asyncio.sleep(1)

    @commands.command()
    async def rare(self, ctx):
        db_obj = db.DBHandler()
        word = await db_obj.fetch_random_word()
        result = await scrapers.DictionaryThings.get_word(word[1])

        await ctx.send(f"**VOTRE MOT RARE, BOSS**\n\n:book: {result}")

    @commands.command(aliases=['ce', 'brain', 'getwo'])
    async def cerveau(self, ctx, *, message=None):
        if not message:
            await ctx.send("Certes, mais que dois-je vous rappeler ? (EXEMPLE : !cerveau MESSAGE 09h10)")

        else:
            try:
                rappel, reminder_time = reminder_format(message)
                await ctx.send(":pencil: Rappel enregistré ! ")
                await asyncio.sleep(reminder_time)
                user = ctx.message.author
                await user.send(f":pencil: **RAPPEL :** {rappel}")
            except:
                await ctx.send("Erreur de format ou de Sen. EXEMPLE : !cerveau MESSAGE 09h10")
        
    @commands.command(aliases=['am'])
    async def ajoutermot(self, ctx, arg=None):
        if not arg:
            await ctx.send("Il vous faut, faquin(e), ajouter un mot et non du rien.")
            return

        word = await scrapers.DictionaryThings.get_word(arg)

        if not word:
            await ctx.send("Le mot n'existe pas. HONTE.")
            return
        else:
            db_obj = db.DBHandler()
            try:
                db_obj.insert_into_table("rare_words", [arg.lower(), ])
                await ctx.send(f"Le mot {arg} a bien été enregistré.")
            except:
                await ctx.send("Le mot que vous tentez d'ajouter existe déjà (ou Sen ne sait pas coder).")

    ############# Dictionaries and stuff
    @commands.command(aliases=['def'])
    async def post_definition(self, ctx, arg=None):
        if not arg:
            await ctx.send("Il vous faut, faquin(e), ajouter un mot et non du rien.")
            return

        word = await scrapers.DictionaryThings.get_word(arg)
        
        if word == False:
            await ctx.send("Ce mot n'existe pas.")
        else:
            await ctx.send(word)

    #### Utils

        formatted = []

        for avis in result:
            user = await self.bot.fetch_user(int(avis[1]))
            avis = avis[3]
            if avis[-1] == 1:
                formatted.append(f":sparkles: [RECOMMANDATION] {user.name}: {avis}")
            else:
                formatted.append(f":book: {user.name}: {avis}")
                

        return "\n\n".join(formatted)
"Survoûter"

async def setup(bot):
    await bot.add_cog(Productivity(bot))