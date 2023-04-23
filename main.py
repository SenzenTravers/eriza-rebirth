import random

from decouple import config
import discord
from discord.ext import commands

from cogs.utils.resources import desapprobation, jesus

class Eriza(commands.Bot):        
    async def on_ready(self):
        print(f'Bonjour, {self.user}')
        await self.load_extension('cogs.coureur')
        await self.load_extension('cogs.shitpost')
        await self.load_extension('cogs.configurateur')

intents = discord.Intents.all()
bot = Eriza(command_prefix="!", help_command = None, intents=intents)


@bot.listen('on_message')
async def on_message(message):
    msg = message.content.lower()

    if message.author == bot.user:
        return
    
    elif msg.startswith('eriza'):
        answers = ["C'est bien moi :D", ":heart:", ">:3", "... Jésus ?", "Sen coupable"]
        await message.channel.send(random.choice(answers))

    elif "jesus" in msg or "jésus" in msg:
        await message.channel.send(random.choice(jesus))

    elif 'merci, eriza' in msg or "merci eriza" in msg:
        await message.channel.send("De rien :D")

    if message.author.id == 326467419562311680:
        chance = random.choice(range(200))
        if chance > 197:
            await message.channel.send(random.choice(desapprobation))

client_secret = config("client_secret")
bot.run(client_secret)