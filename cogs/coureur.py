import asyncio
import datetime as dt
import random

import discord
from discord.ext import commands

from .utils.time_handler import *
from .utils.coureurs_texts import SprintEndText
from .utils.coureur_handler import Course
from .utils.db import DBHandler


class Coureur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sprint = False
        self.runners = {}
        self.enders = {}
        self.course = Course([], False)

    @commands.command(aliases=["x"])
    async def bleh(self, ctx, *arg):
        db_handler = DBHandler()
        server_id = ctx.message.guild.id

        stuff = await db_handler.fetch_from_table(
            "sprints",
            "server_id",
            server_id,
            ctx=ctx
        )
        await ctx.channel.send(stuff)

    @commands.command(aliases=['c'])
    async def course(self, ctx, *arg):
        course_data = self.course.launch_course(arg)
        await ctx.send(course_data[1])

        if course_data[0] == 1:
            duration = course_data[2]
            await asyncio.sleep(120)
            started_course = self.course.start_course(duration)
            await ctx.send(started_course[1])

            if started_course[0] == 1:
                await asyncio.sleep(duration*60)

                every_wordcount = self.course.ask_for_wordcount()
                await ctx.channel.send(every_wordcount)
                await asyncio.sleep(120)

                results = self.course.finish_course()
                await ctx.send(results)

    @commands.command(aliases=['cm'])
    async def mots(self, ctx, *arg):
        answer = self.course.participant_give_final_wordcount(
            {"name": ctx.message.author,
             "wordcount": arg[0]}
        )
        await ctx.send(answer[1])

        # error_no_sprint = "Aucune course en cours."
        # error_words = "Format: ```!j 1000``̀`̀"
        # error_not_in = "Vous ne faites pas partie de cette course. IMPOSTRICE."
        # words = 0
        # user = ctx.message.author

        # if self.sprint == False:
        #     await ctx.channel.send(error_no_sprint)
        # elif user not in self.runners.keys():
        #     await ctx.channel.send(error_not_in)
        # elif arg:
        #     if not arg[0].isdigit():
        #         await ctx.channel.send(error_words)
        #     else:
        #         words = int(arg[0])
        #         self.enders.update({user: words})
        #         await ctx.channel.send(f"{user.name}, votre dernier mot : {words} mots.")

    @commands.command(aliases=['cj'])
    async def joindre(self, ctx, *arg):
        answer = self.course.participant_is_joining(
            {"name": ctx.message.author,
             "wordcount": arg}
        )
        await ctx.send(answer[1])

    def winners_list(self):
        #TODO : sort thanks to a lambda function of self.enders[user_results[0]] - user_results[1]
        sorted_users = sorted(self.runners.items(), key=lambda item: item[1])
        sorted_users.reverse()
        cleaned_users = []

        for user_results in sorted_users:
            # LUCILE : le bug est ici
            written_words = self.enders[user_results[0]] - user_results[1]
            user_results = list(user_results)
            user_results.append(written_words)
            user_results[1] = self.enders[user_results[0]]
            cleaned_users.append(user_results)

            if written_words > 0:
                sorted_users = [
                    f"\n:star2: {item[0].mention}: {item[1]} mots, dont {item[2]} nouveaux !" for item in cleaned_users]
            elif written_words == 0:
                sorted_users = [f"\n:star2: {item[0].mention} {random.choice(SprintEndText.zero_words)}" for item in cleaned_users]
            else:
                sorted_users = [f"\n:star2: {item[0].mention} a effacé {written_words} mots." for item in cleaned_users]

        if len(self.enders.keys()) > 1:
            sorted_users_list = "".join(sorted_users)
        else:
            sorted_users_list = f"""{sorted_users[0]}
            
{random.choice(SprintEndText.sprint_alone)}
            """

        return sorted_users_list

    @commands.command(aliases=['s'])
    async def session(self, ctx, *arg):
        sprint_data = return_delays(arg)
        start_time = sprint_data[2]
        duration = int(sprint_data[1]/60)

        if start_time.minute < 10:
            await ctx.channel.send(f"La session commencera à {start_time.hour}h0{start_time.minute} pour {duration} minutes.")
        else:
            await ctx.channel.send(f"La session commencera à {start_time.hour}h{start_time.minute} pour {duration} minutes.")

        await asyncio.sleep(sprint_data[0])

async def setup(bot): # set async function
    await bot.add_cog(Coureur(bot)) # Use await