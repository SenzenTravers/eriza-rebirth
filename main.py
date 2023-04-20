import random

from decouple import config
import discord
from discord.ext import commands

from cogs import coureur, shitpost


class Eriza(commands.Bot):        
    async def on_ready(self):
        print(f'Bonjour, {self.user}')
        await self.add_cog(coureur.Coureur(bot))
        await self.add_cog(shitpost.Shitpost(bot))


intents = discord.Intents.all()
bot = Eriza(command_prefix="!", intents=intents)

@bot.listen('on_message')
async def on_message(message):
    msg = message.content.lower()
    jesus = ["JÉSUS !!!", "https://tenor.com/view/jesus-christ-wink-smile-jesus-gif-15483760",
             "JÉSUS :D :D :D", "*murmure* Jésus.....", "... Jésus ?", "Jésus ewe",
             "Jésuuuuuuuuuuuuus", "*Djézouss*", "https://tenor.com/view/jesus-peeking-i-see-you-guilty-gif-25117299",
             "Jésus ! ;3", "J É S U S", "𝒥𝑒𝓈𝓊𝓈", "ʆЄƧƲƧ", "🐺♣  ן乇𝐬𝓤s  🐒🐳",
             "イエス", "JÉSUS :weary:", "Jezus... (avec l'accent polonais)",
             "Jesus ! (avec l'accent danois)", "*Rézous*",
             "Je le sais bien, que vous blasphémez è_é"]

    if message.author == bot.user:
        return
    
    if message.author.id == 326467419562311680:
        desapprobation = [":zn:", ":offense:",
            "INÉDIT : une majorité des Français ne voteraient pas pour Sen aux présidentielles 2024",
            ">: (", "Sen a tort", "Beurk, une Sen", "*Sen slander*",
            "Eh bien JE DÉSAPPROUVE", ":black_heart:"]
        chance = random.choice(range(200))
        if chance > 197:
            await message.channel.send(random.choice(desapprobation))

    if msg.startswith('eriza'):
        answers = ["C'est bien moi :D", ":heart:", ">:3", "... Jésus ?", "Sen coupable"]
        await message.channel.send(random.choice(answers))

    if "jesus" in msg or "jésus" in msg:
        await message.channel.send(random.choice(jesus))

client_secret = config("client_secret")
bot.run(client_secret)