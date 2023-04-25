import asyncio
import datetime as dt
import random

import discord
from discord.ext import commands

from .utils.coureur import *
from .utils.coureurs_texts import *


class Coureur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sprint = False
        self.runners = {}
        self.enders = {}

    @commands.command(aliases=['c'])
    async def course(self, ctx, *arg):
        error_format = """
        Merci de formater votre message de la façon suivante :
        ```course à 15 pour 30``` (unités en minutes)
        """ 
        error_already_course = "Un marathon d'écriture est déjà en cours !"

        sprint_data = return_delays(arg)
        start_time = sprint_data[2]
        duration = int(sprint_data[1]/60)

        if self.sprint:
            await ctx.channel.send(error_already_course)
        elif sprint_data == False:
            await ctx.channel.send(error_format)
        else:
            self.sprint = True
            if start_time.minute < 10:
                await ctx.channel.send(f"Le marathon commencera à {start_time.hour}h0{start_time.minute} pour {duration} minutes.")
            else:
                await ctx.channel.send(f"Le marathon commencera à {start_time.hour}h{start_time.minute} pour {duration} minutes.")
            await asyncio.sleep(sprint_data[0])
            
            if self.runners == {}:
                self.sprint = False
                await ctx.channel.send(random.choice(sprint_cancelled))
            else:
                mentions = ", ".join([dude.mention for dude in self.runners.keys()])
                await ctx.channel.send(f"""{mentions}
:sparkles::sparkles::sparkles: **Un, deux, trois, GO** !:sparkles::sparkles::sparkles:
                
Vous avez {duration} minutes !""")
                await asyncio.sleep(sprint_data[1])

                mentions = ", ".join([dude.mention for dude in self.runners.keys()])
                await ctx.channel.send(f"{mentions}\nABOULEZ LES MOTS ! Vous avez deux (2) minutes.")
                await asyncio.sleep(120)
                finished_list = self.winners_list()
                self.sprint = False
                self.coureurs = {}
                self.enders = {}

                results = "\n:sparkles::sparkles::sparkles: **C'EEEEEEST *FINI***:sparkles::sparkles::sparkles:" + \
                    f"\n\n{finished_list}\n\n{random.choice(inspiring_quotes)}"
                await ctx.channel.send(results)

    @commands.command(aliases=['cm'])
    async def mots(self, ctx, *arg):
        error_no_sprint = "Aucune course en cours."
        error_words = "Format: ```!j 1000``̀`̀"
        error_not_in = "Vous ne faites pas partie de cette course. IMPOSTRICE."
        words = 0
        user = ctx.message.author

        if self.sprint == False:
            await ctx.channel.send(error_no_sprint)
        elif user not in self.runners.keys():
            await ctx.channel.send(error_not_in)
        elif arg:
            if not arg[0].isdigit():
                await ctx.channel.send(error_words)
            else:
                words = int(arg[0])
                self.enders.update({user: words})
                await ctx.channel.send(f"{user.name}, votre dernier mot : {words} mots.")

    @commands.command(aliases=['cj'])
    async def joindre(self, ctx, *arg):
        error_no_sprint = "Aucune course en cours."
        error_words = "Format: ```!j 1000``̀`̀"
        user = ctx.message.author
        words = 0
        
        if self.sprint == False:
            await ctx.channel.send(error_no_sprint)
        else:
            if arg:
                if not arg[0].isdigit():
                    await ctx.channel.send(error_words)
                else:
                    words = int(arg[0])

            self.runners.update({user :words})
            self.enders.update({user :words})
            await ctx.channel.send(f"{user.name} joint avec {words} mots.")

    def winners_list(self):
        sorted_users = sorted(self.runners.items(), key=lambda item: item[1])
        sorted_users.reverse()
        cleaned_users = []

        for user_results in sorted_users:
            written_words = self.enders[user_results[0]] - user_results[1]
            user_results = list(user_results)
            user_results.append(written_words)
            user_results[1] = self.enders[user_results[0]]
            cleaned_users.append(user_results)

            if written_words > 0:
                sorted_users = [
                    f"\n:star2: {item[0].mention}: {item[1]} mots, dont {item[2]} nouveaux !" for item in cleaned_users]
            elif written_words == 0:
                sorted_users = [f"\n:star2: {item[0].mention} {random.choice(zero_words)}" for item in cleaned_users]
            else:
                sorted_users = [f"\n:star2: {item[0].mention} a effacé {written_words} mots." for item in cleaned_users]

        if len(self.enders.keys()) > 1:
            sorted_users_list = "".join(sorted_users)
        else:
            sorted_users_list = f"""{sorted_users[0]}
            
{random.choice(sprint_alone)}
            """

        return sorted_users_list


async def setup(bot): # set async function
    await bot.add_cog(Coureur(bot)) # Use await