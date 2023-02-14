import discord
from discord.ext import commands

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief = "bye bye!") # we can also add application commands
    async def goodbye(self, ctx):
        await ctx.send('Berlock bye bye!')

    @commands.command()
    async def popularloner(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.channel.send("A dude who's an athlete, hot and everyone thinks he actually gets lots of pussy, but he's actually chill, kinda vibes, really vibey when stoned and can't get no pussy")

    @commands.command()
    async def indie(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.channel.send("imagine how much happier the world would be if more people chucked on a comfy fit (i personally like to go for the granola dad look), grabbed an iced oat latte and went to watch the sunset with their fav indie tunes blasting in the background.")

    @commands.command()
    async def normal(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.channel.send("is there still room for normal guys in society? i’m not a skater, alt boy, indie, jock, artist,… i’m just….. normal …i wear baseball hats… i wear hoodies … just a normal guy. And somehow i feel like i just…, don’t belong")

    @commands.command()
    async def O(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.channel.send("NGUYEN!")

    @commands.command()
    async def statement(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.channel.send('What the fuck, why the fuck, and as for who the fuck it’s 100% Alice Sauter"')

    @commands.command()
    async def cannibal(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.channel.send('```"Yes! It’ll be a meal full of delicious cruelty and greed" -Big Money\'s Redemption#6969```')

    @commands.command()
    async def sirens(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.channel.send('```"what\'s with the sirens? Is that world\'s end?  I want to be the mahatma of that siren voice, tell me how I should go about being a better person. What else can we do besides eating her?" -ExPeri3nce#0034```')

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Memes(bot)) # add the cog to the bot
