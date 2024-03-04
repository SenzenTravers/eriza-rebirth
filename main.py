import random

from decouple import config
import discord
from discord.ext import commands

from cogs.utils.resources import desapprobation, jesus

class Eriza(commands.Bot):
    async def setup_hook(self):
        await self.load_extension('cogs.configurateur')
        await self.load_extension('cogs.coureur')
        await self.load_extension('cogs.productivity')
        # await self.load_extension('cogs.shards')
        await self.load_extension('cogs.shitpost')

    async def on_ready(self):
        print(f'Je suis {self.user} et je VIS :D')

intents = discord.Intents.all()
activity = discord.Activity(
    name='!aide',
    type=discord.ActivityType.watching
)
bot = Eriza(command_prefix="!",
    help_command = None,
    intents=intents,
    activity=activity)

@bot.listen('on_message')
async def on_message(message):
    msg = message.content.lower()

    if message.author == bot.user:
        return
    
    elif msg.startswith('eriza'):
        chance = random.choice(range(100))
        if chance > 98:
            answers = [
                "C'est bien moi :D", ":heart:", ">:3", "... Jésus ?", "Sen coupable"
            ]
            await message.channel.send(random.choice(answers))

    elif "jesus" in msg or "jésus" in msg:
        await message.channel.send(random.choice(jesus))

    elif "erza" in msg:
        erza = ["ERIZA. C'est ERIZA.", "Eriza.", "*offense silencieuse*"]
        await message.channel.send(random.choice(erza))

    elif 'pardon, eriza' in msg or "pardon eriza" in msg:
        sorry = ["Tout est pardonné :)", "Pas de souci......",
            "Vas ; je ne te hais point.", "Aucun problème ! :>",
            "Jésus prêche le pardon, donc je pardonne (mais n'en pense pas moins).",
            "Pas de souci <3"]
        await message.channel.send(random.choice(sorry))

    elif 'merci, eriza' in msg or "merci eriza" in msg:
        await message.channel.send("De rien :D")

    elif (
        'jtm, eriza' in msg or "jtm eriza" in msg
        or "je t'aime eriza" in msg or "je t'aime, eriza" in msg
        ):
        ilu = ["Moi non", "Je suis désolée, mais... Je suis un bot.",
            "Tout ceci ne t'arriverait pas si tu te concentrais sur le J-man",
            "no", "Pas devant les enfants, voyons !",
            "MAMAAAAAN, ON M'INDÉCENTISE èé"
            ]
        await message.channel.send(random.choice(ilu))

    if message.author.id == 326467419562311680:
        chance = random.choice(range(300))
        if chance > 298:
            await message.channel.send(random.choice(desapprobation))

client_secret = config("client_secret")

bot.run(client_secret)