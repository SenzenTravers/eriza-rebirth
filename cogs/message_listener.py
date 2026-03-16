import random

from discord.ext import commands

from .utils.resources import JsonLoader


class MessageListener(commands.Cog):
    BOT_AUTHOR_ID = 326467419562311680
    CIELLY_ID = 311408924504883201

    def __init__(self, bot):
        self.bot = bot
        self.replier = JsonLoader("replies")

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content.lower()

        if message.author == self.bot.user:
            return
        
        ctx = message.channel
        if message.author.id == MessageListener.BOT_AUTHOR_ID:
            chance = random.choice(range(500))
            if chance > 498:
                await ctx.send(self.replier.get_random("disapproval"))
                return
        elif message.author.id == MessageListener.CIELLY_ID and ("ferdinand" in msg or "ferdie" in msg):
                await ctx.send(self.replier.get_random("ferdinand"))
                return

        if msg.startswith('eriza'):
            chance = random.choice(range(100))
            if chance > 98:
                await ctx.send(self.replier.get_random("name_called"))
        elif "jesus" in msg or "jésus" in msg:
            await ctx.send(self.replier.get_random("jesus"))
        elif "erza" in msg:
            await ctx.send(self.replier.get_random("erza"))
        elif 'pardon, eriza' in msg or "pardon eriza" in msg:
            await ctx.send(self.replier.get_random("sorry"))
        elif 'merci, eriza' in msg or "merci eriza" in msg:
            await ctx.send("De rien :D")
        elif (
            'jtm, eriza' in msg or "jtm eriza" in msg
            or "je t'aime eriza" in msg or "je t'aime, eriza" in msg
            ):
            await ctx.send(self.replier.get_random("love_confession"))


async def setup(bot):
    await bot.add_cog(MessageListener(bot))