import discord
from discord.ext import commands, bridge
import berlock_gpt
from Quote2Image import Convert, ImgObject

class GPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command(brief = "cat")
    async def cat(self, ctx, text):
        cat_text = berlock_gpt.newcatGPT(text)
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.respond(cat_text)
        await ctx.message.add_reaction(emoji)

    @bridge.bridge_command(brief = "CATify")
    async def catify(self, ctx, text):
        cat_text = berlock_gpt.newcatGPT(text)
        embed = discord.Embed(title="Blight AI",
                              url="https://zombo.com",
                          colour=0xe81feb)
        embed.set_author(name="Berlock Bot",
                         icon_url="https://images-ext-2.discordapp.net/external/XaZD0LjdRFtLqJKRHD96hbM3Yrxo0Nr2bQrkz2yN7Uk/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/1027808278551461988/d9ce0c74f3aa9fb61e44fb9b186dd9bd.png")
        embed.add_field(name="Catify =^._.^=",
                        value=f"```test```")
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

    @commands.message_command(name = "CATify message")
    async def catify_message2(self, ctx, text: discord.Message):
        cat_text = berlock_gpt.newcatGPT(text.content)
        await ctx.respond(cat_text)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(GPT(bot)) # add the cog to the bot
