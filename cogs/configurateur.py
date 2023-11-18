import asyncio
import os

import discord
from discord.ext import commands

from .utils.help_texts import *

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='reload', description="Reload all/one of the bots cogs!"
    )
    @commands.is_owner()
    async def reload(self, ctx, cog=None):
        if not cog:
            # No cog, means we reload all cogs
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    color=0x808080,
                    timestamp=ctx.message.created_at
                )
                for ext in os.listdir("./cogs/"):
                    if ext.endswith(".py") and not ext.startswith("configurateur"):
                        try:
                            await self.bot.reload_extension(f"cogs.{ext[:-3]}")
                            embed.add_field(
                                name=f"Reloaded: `{ext}`",
                                value='\uFEFF',
                                inline=False
                            )
                        except Exception as e:
                            embed.add_field(
                                name=f"Failed to reload: `{ext}`",
                                value=e,
                                inline=False
                            )
                        await asyncio.sleep(0.5)
                await ctx.send(embed=embed)
        else:
            # reload the specific cog
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    color=0x808080,
                    timestamp=ctx.message.created_at
                )
                ext = f"{cog.lower()}.py"
                if not os.path.exists(f"{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"Failed to reload: `{ext}`",
                        value="This cog does not exist.",
                        inline=False
                    )

                elif ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        await self.bot.reload_extension(f"cogs.{ext[:-3]}")
                        embed.add_field(
                            name=f"Reloaded: `{ext}`",
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception:
                        embed.add_field(
                            name=f"Failed to reload: `{ext}`",
                            inline=False
                        )
                await ctx.send(embed=embed)

    @commands.command(description="Annule le sprint en cours.")
    async def annuler(self, ctx):
        await self.bot.reload_extension(f"cogs.coureur")
        await ctx.send("Le spr... La course a été annulée.")

    @commands.command(
        aliases=["help"],
        description="La fonctionnalité d'aide, tiens.")
    async def aide(self, ctx):
        embed = discord.Embed(
            title="(À l')Aide",
            color=0x808080,
            timestamp=ctx.message.created_at
        )

        embed.add_field(
            name="**SESSIONS D'ÉCRITURE**",
            value=coureur_text,
            inline=False
        )

        embed.add_field(
            name="**PRODUCTIVITÉ (sisi)**",
            value=productivity_text,
            inline=False
        )

        embed.add_field(
            name="**CHOSES SÉRIEUSES**",
            value=shitpost_text,
            inline=False
        )
        await ctx.send(embed=embed)

async def setup(bot): # set async function
    await bot.add_cog(Config(bot)) # Use await