import asyncio
import datetime as dt
import random

import discord

from discord.ext import commands, tasks

from .utils import avis, db, scrapers

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

            for contest in contests:
                user = ctx.message.author
                await user.send(contest)

    # LOUCIL
    # @commands.command(aliases=['co'])
    # async def commenter(self, ctx, *arg):
    #     """
    #     Permet de donner un avis sur un bouquin
    #     """
    #     def answer(msg):
    #         if msg.channel == ctx.channel and msg.author == ctx.author:
    #             return msg.content.lower() in ("oui", "o", "non", "b")

    #     def get_opinion(msg):
    #         return msg.channel == ctx.channel and msg.author == ctx.author and msg.content.startswith("=")

    #     book = await self.handle_avis(ctx, arg)

    #     if not book:
    #         ctx.send("Désolée ; cet ouvrage est le fruit de votre imagination échevelée.")

    #     try:
    #         await ctx.send("Voulez-vous écrire un avis sur ce livre ? (O/Oui/N/Non)")
    #         check_answer = await self.bot.wait_for('message', check=answer, timeout = 60.0)

    #         if check_answer.content.lower() in ("oui", "o"):
    #             try:
    #                 is_rec = False
    #                 await ctx.send("Veuillez maintenant écrire votre avis en le préfixant par =")
    #                 wait_opinion = await self.bot.wait_for(
    #                     'message',
    #                     check=get_opinion,
    #                     timeout = 60.0
    #                     )
                    
    #                 await ctx.send("Est-ce une rec ? (o/oui, n/non)")
    #                 wait_rec = await self.bot.wait_for(
    #                         'message',
    #                         check=answer,
    #                         timeout = 30.0
    #                         )

    #                 if wait_rec.content.lower() in ("o", "oui"):
    #                     is_rec = True

    #                 db_handler = db.DBHandler()
    #                 try:
    #                     await db_handler.insert_into_table("books", [book["link"]])
    #                 except:
    #                     pass

    #                 db_handler2 = db.DBHandler()
    #                 book_id = db_handler2.fetch_from_table("books", "link", book["link"])
                    
    #                 db_handler3 = db.DBHandler()
    #                 if is_rec == True:
    #                     db_handler3.insert_into_table(
    #                         "recs",
    #                         [ctx.author.id, book_id[0], wait_opinion.content[1:], 1]
    #                     )
    #                 else:
    #                     db_handler3.insert_into_table(
    #                         "recs",
    #                         [ctx.author.id, book_id[0], wait_opinion.content[1:], 0]
    #                     )

    #                 await ctx.send("Votre avis a bien été enregistré.")

    #             except asyncio.TimeoutError: 
    #                 return

    #         elif check_answer.content.lower() in ("non", "n"):
    #             answer_avis = [
    #                 "Ok.", "Eh bien bonne journée", "C'est bien compréhensible.",
    #                 "Mes attentes, déçues............"
    #             ]
    #             await ctx.send(random.choice(answer_avis))

    #     except asyncio.TimeoutError: 
    #         return

    # LOUCIL
    # @commands.command(aliases=['va'])
    # async def voiravis(self, ctx, *arg):
    #     book = await self.handle_avis(ctx, arg)

    #     if not book:
    #         await ctx.send("Désolée, mais ce livre est un mythe.")

    #     db_handler = db.DBHandler()
    #     book_id = db_handler.fetch_from_table("books", "link", book["link"])[0]
    #     db_handler2 = db.DBHandler()
    #     avis = db_handler2.fetch_from_table("recs", "book_id", book_id, many=True)
    #     formatted_avis = await self.format_avis(avis)

    #     await ctx.send(formatted_avis)

    # @commands.command(aliases=['vl'])
    # TODO: Un jour, fonction recherche de livre
    # async def voirlivres(self, ctx, *arg):
    #     db_handler = db.DBHandler()
    #     books = db_handler.fetch_all_from_table("books")

    #     for book in books:
    #         lookuper = avis.BookSifter()
    #         rec = await lookuper.look_up(book[1])
    #         print(rec)

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
    async def handle_avis(self, ctx, arg):
        """
        Return False if something is wrong. Else, return rec.
        """
        if not arg:
            answer = "Tenter de chercher le rien... Très post-moderne."
            await ctx.channel.send(answer)

        elif len(arg) <= 2:
            await ctx.channel.send("Merci de préciser un titre ET un auteur.")
        else:
            lookuper = avis.BookSifter()
            rec = await lookuper.look_up(arg)

            if type(rec) != str:
                if len(rec["authors"]) == 1:
                    formatted = f"**{rec['title']}**, par {rec['authors'][0]}\n{rec['link']}"
                else:
                    authors = await lookuper.deal_with_authors(rec["authors"])
                    formatted = f"**{rec['title']}**, par {authors}\n{rec['link']}"

                await ctx.channel.send(formatted)

            return rec
        
        return False

    async def format_avis(self, result):
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