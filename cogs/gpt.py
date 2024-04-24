import discord
from discord.ext import commands, bridge
import berlock_gpt
from Quote2Image import Convert, ImgObject

class GPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command(brief = "CATify")
    async def catify(self, ctx, text):
        cat_text = berlock_gpt.newcatGPT(text)
        embed = discord.Embed(title="Blight AI",
                              url="https://zombo.com",
                          colour=0xe81feb)
        embed.set_author(name="Berlock Bot",
                         icon_url="https://images-ext-2.discordapp.net/external/XaZD0LjdRFtLqJKRHD96hbM3Yrxo0Nr2bQrkz2yN7Uk/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/1027808278551461988/d9ce0c74f3aa9fb61e44fb9b186dd9bd.png")
        embed.add_field(name="Catify =^._.^=",
                        value=f"```{cat_text}```")
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.respond(embed = embed)
        await ctx.message.add_reaction(emoji)

    @commands.message_command(name = "CATify message")
    async def catify_message(self, ctx, text: discord.Message):
        cat_text = berlock_gpt.newcatGPT(text.content)
        embed = discord.Embed(title="Blight AI",
                              url="https://zombo.com",
                          colour=0xe81feb)
        embed.set_author(name="Berlock Bot",
                         icon_url="https://images-ext-2.discordapp.net/external/XaZD0LjdRFtLqJKRHD96hbM3Yrxo0Nr2bQrkz2yN7Uk/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/1027808278551461988/d9ce0c74f3aa9fb61e44fb9b186dd9bd.png")
        embed.add_field(name="Catify =^._.^=",
                        value=f"```{cat_text}\n\n -{text.author.name}cat```")
        await ctx.respond(embed = embed)

    @bridge.bridge_command(brief = "Berlockian Wisdom")
    async def berlock(self, ctx, text):
        user_text = berlock_gpt.berlockGPT(text)
        embed = discord.Embed(title="Blight AI",
                              url="https://zombo.com",
                          colour=0xe81feb)
        embed.set_author(name="Berlock Bot",
                         icon_url="https://images-ext-2.discordapp.net/external/XaZD0LjdRFtLqJKRHD96hbM3Yrxo0Nr2bQrkz2yN7Uk/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/1027808278551461988/d9ce0c74f3aa9fb61e44fb9b186dd9bd.png")
        embed.add_field(name="Berlock's Wisdom",
                        value=f"```{user_text}```")
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.respond(embed = embed)
        await ctx.message.add_reaction(emoji)

    @bridge.bridge_command(brief = "grubworld")
    async def grubworld(self, ctx, text):
        grub_text = berlock_gpt.grubGPT(text)
        embed = discord.Embed(title="Blight AI",
                              url="https://zombo.com",
                          colour=0xe81feb)
        embed.set_author(name="Berlock Bot",
                         icon_url="https://images-ext-2.discordapp.net/external/XaZD0LjdRFtLqJKRHD96hbM3Yrxo0Nr2bQrkz2yN7Uk/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/1027808278551461988/d9ce0c74f3aa9fb61e44fb9b186dd9bd.png")
        embed.add_field(name="Grubworld",
                        value=f"```{grub_text}```")
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.respond(embed = embed)
        await ctx.message.add_reaction(emoji)

    @bridge.bridge_command(brief = "Lord Grubbington's Wisdom")
    async def grubbington(self, ctx, text):
        grub_text = berlock_gpt.grubbingtonGPT(text)
        embed = discord.Embed(title="Grubbington's Wisdom",
                              url="https://zombo.com",
                          colour=0x6A4A3F)
        embed.set_author(name="The Honorable Lord Grubbington",
                         icon_url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8aa98588-c6d6-4070-84dc-1377a903e813/d85tkr7-6eaf66f5-2025-40d9-af31-9fb3c5009ef6.jpg/v1/fit/w_600,h_690,q_70,strp/grub_cartoon___terranem_nematodes_by_growngraphic_d85tkr7-375w-2x.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzhhYTk4NTg4LWM2ZDYtNDA3MC04NGRjLTEzNzdhOTAzZTgxM1wvZDg1dGtyNy02ZWFmNjZmNS0yMDI1LTQwZDktYWYzMS05ZmIzYzUwMDllZjYuanBnIiwiaGVpZ2h0IjoiPD02OTAiLCJ3aWR0aCI6Ijw9NjAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLndhdGVybWFyayJdLCJ3bWsiOnsicGF0aCI6Ilwvd21cLzhhYTk4NTg4LWM2ZDYtNDA3MC04NGRjLTEzNzdhOTAzZTgxM1wvZ3Jvd25ncmFwaGljLTQucG5nIiwib3BhY2l0eSI6OTUsInByb3BvcnRpb25zIjowLjQ1LCJncmF2aXR5IjoiY2VudGVyIn19.OlcG-B4QcphqEIIushaz9TkLNSX41qmL-jy4oeNzHww")
        embed.add_field(name="Grubworld",
                        value=f"{grub_text}")
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.respond(embed = embed)
        await ctx.message.add_reaction(emoji)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(GPT(bot)) # add the cog to the bot
