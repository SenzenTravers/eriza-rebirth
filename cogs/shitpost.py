import discord
from discord.ext import commands

from .utils.shitpost import *
from .utils.resources import dimitri, gego, geto, gojo, laments, nanami, sensim


class Shitpost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["d", "D"])
    async def drama(self, ctx):
        await ctx.send("https://tenor.com/view/dramatic-chipmunk-gif-19778021")

    @commands.command()
    async def dimitri(self, ctx):
        user = ctx.message.author
        await user.send(random.choice(dimitri))

    @commands.command()
    async def fic(self, ctx, *, message=None):
        if message == None:
            message = "Filez-moi un pairing à ficcer, mécréant !"
        else:
            message = fanfic_it(message)

        await ctx.send(message)

    @commands.command()
    async def folamour(self, ctx):
        speak = ["Et si tu lui parlais ?", "PARLE-LUI",
            "Mais as-tu pensé à... lui parler ?",
            "https://tenor.com/view/you-better-start-talking-cordell-walker-walker-texas-ranger-speak-now-let-me-hear-it-gif-1894414266930324422",
            "https://tenor.com/view/speakup-talk-cat-speak-up-cute-gif-1570144500718911029",
            "https://tenor.com/view/go-talk-to-him-ella-payne-house-of-payne-wing-woman-go-see-him-gif-19162362",
            "*susurre* Parle-lui", "Paaaaaaaaaaaaaarrrrrrrle-lllluuuuuuuiiiiiiiiii", "Hypothèse : tu lui parles.", "nick"
        ]
        talk = random.choice(speak)

        if talk == "nick":
            guild = self.bot.get_guild(ctx.message.guild.id)
            queenie = guild.get_member(305418034112233492)
            await queenie.edit(nick="PARLE-LUI")
        else:
            await ctx.send(talk)

    @commands.command()
    async def gego(self, ctx):
        user = ctx.message.author
        await user.send(random.choice(gego))

    @commands.command()
    async def geto(self, ctx):
        user = ctx.message.author
        await user.send(random.choice(geto))

    @commands.command(aliases=['g', 'G'])
    async def gojo(self, ctx):
        user = ctx.message.author
        await user.send(random.choice(gojo))

    @commands.command()
    async def nanami(self, ctx):
        user = ctx.message.author
        await user.send(random.choice(nanami))

    @commands.command(aliases=['o', 'O'])
    async def ouin(self, ctx):
        await ctx.send(random.choice(laments))

    @commands.command(aliases=['q', 'Q'])
    async def queenie(self, ctx, *, message=None):
        if message == None:
            message = "Certes, mais que dois-je quueener ?"
        else:
            message = f"Ainsi parla Queenie : {queenize(message)}"
        await ctx.send(message)

    @commands.command()
    async def cielly(self, ctx, *, message=None):
        if message == None:
            message = "Certes, mais que dois-je cieller ?"
        else:
            message = f"Ainsi parla Cielly : {queenize(message)}"
        await ctx.send(message)

    @commands.command()
    async def sen(self, ctx):
        await ctx.send(random.choice(sensim))

    @commands.command()
    async def sne(self, ctx):
        await ctx.send(queenize(random.choice(sensim)))


async def setup(bot): # set async function
    await bot.add_cog(Shitpost(bot)) # Use await