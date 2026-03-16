import discord
from discord.ext import commands

from .utils.resources import JsonLoader, MPSender
from .utils.ressources_yaoi import YaoiGenerator
from .utils.shitpost import *

class Shitpost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.replier = JsonLoader('nonsense_replies')

    @commands.command()
    async def dimitri(self, ctx):
        await MPSender.send_mp(ctx, self.replier.get_random("dimitri"))

    @commands.command(aliases=["d", "D"])
    async def drama(self, ctx):
        await ctx.send(self.replier.get_random("drama"))

    @commands.command()
    async def gego(self, ctx):
        await MPSender.send_mp(ctx, self.replier.get_random("gego"))

    @commands.command()
    async def geto(self, ctx):
        await MPSender.send_mp(ctx, self.replier.get_random("geto"))

    @commands.command(aliases=['g', 'G'])
    async def gojo(self, ctx):
        await MPSender.send_mp(ctx, self.replier.get_random("gojo"))

    @commands.command()
    async def nanami(self, ctx):
        await MPSender.send_mp(ctx, self.replier.get_random("nanami"))

    @commands.command(aliases=['o', 'O'])
    async def ouin(self, ctx):
        await ctx.send(self.replier.get_random("ouin"))

    @commands.command()
    async def fic(self, ctx, *, pairing=None):
        message = fanfic_it(pairing) if pairing else "Filez-moi un pairing à ficcer, mécréant !"
        await ctx.send(message)

    @commands.command()
    async def yaoi(self, ctx):
        prompt = YaoiGenerator.return_random_prompt()

        await ctx.send(f"Les divinités du yaoi ont choisi...\n\n```{prompt}```")

    @commands.command(aliases=['q', 'Q'])
    async def queenie(self, ctx, *, message=None):
        if message == None:
            message = "Certes, mais que dois-je queener ?"
        else:
            message = f"Ainsi parla Queenie : {queenize(message)}"
        await ctx.send(message)

    @commands.command()
    async def sen(self, ctx):
        await ctx.send(self.replier.get_random("sen"))

    @commands.command()
    async def sne(self, ctx):
        await ctx.send(queenize(self.replier.get_random("sen")))

    @commands.command()
    async def pine(self, ctx):
        if random.randint(0, 4) == 3:
            await ctx.send("https://media.discordapp.net/attachments/1252186046335160330/1279357095854080093/20240605_181732.jpg?ex=66d77164&is=66d61fe4&hm=bf041f99e2685bf59c674142082ae06933346ac0da8d5220dbe930d00ff0f1ef&=&format=webp&width=491&height=655")
            return

        channel = self.bot.get_channel(703691008097124402)
        candidates = []
        filler_text = random.choice(
            [
                " IS ABOUT MEEEEEEEEEEEEEEEEEEEEH",
                " IS ABOUT YOUUUUUUUUUUUUUUUUUUUU",
                " est votre kin ! L'astrologie ne ment jamais ! FÉLICITATIONS !",
                " est SO YOU, ma chériiiiie !!",
                ", c'est troooop ton kin, baby",
                " est votre signe astrologique gen Z"
            ]
        )

        async for message in channel.history(limit=20):
            if message.author.id == 432610292342587392 and len(message.embeds) > 0:
                name_char = [message.embeds[0].author.name]
                illustration = message.embeds[0].image.url
                char_dict = {"name": name_char[0], "img": illustration}

                candidates.append(char_dict)
                

        chosen_one = random.choice(candidates)
        await ctx.send(f":star2::star2::star2: **{chosen_one['name']}**{filler_text} :star2::star2::star2:\n\n{chosen_one['img']}")


async def setup(bot):
    await bot.add_cog(Shitpost(bot))