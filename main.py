import discord

from decouple import config
from discord.ext import commands

class Eriza(commands.Bot):
    async def setup_hook(self):
        await self.load_extension('cogs.configurateur')
        await self.load_extension('cogs.coureur')
        await self.load_extension('cogs.productivity')
        # await self.load_extension('cogs.shards')
        await self.load_extension('cogs.shitpost')
        await self.load_extension('cogs.message_listener')

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

client_secret = config("client_secret")
bot.run(client_secret)