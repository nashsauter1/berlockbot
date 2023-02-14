import discord
from discord.ext import commands

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief = "bye bye!") # we can also add application commands
    async def goodbye(self, ctx):
        await ctx.send('Berlock bye bye!')

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Memes(bot)) # add the cog to the bot
