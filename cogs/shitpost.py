import discord
from discord.ext import commands

from .utils.shitpost import *
from .utils.resources import dimitri, gego, geto, gojo, laments, nanami, sensim
from .utils.ressources_yaoi import YaoiGenerator


class Shitpost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["d", "D"])
    async def drama(self, ctx):
        await ctx.send(
            random.choice(
                "https://tenor.com/view/drama-weasel-gif-25999159",
                "https://tenor.com/view/dramatic-music-monkey-piano-drama-gif-5631330",
                "https://tenor.com/view/dun-dun-dun-tykie-tykie-dun-dun-dun-gif-11482815036668846066",
                "https://tenor.com/view/max-rebo-star-wars-music-book-of-boba-fett-music-stops-gif-24461528"
            )
        )

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
    async def yaoi(self, ctx):
        prompt = YaoiGenerator.return_random_prompt()

        await ctx.send(f"Les divinités du yaoi ont choisi...\n\n```{prompt}```")

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

    @commands.command()
    async def pine(self, ctx):
        random_chance = random.randint(0, 4)
        
        if random_chance == 3:
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


async def setup(bot): # set async function
    await bot.add_cog(Shitpost(bot)) # Use await