# Discord bot that sends a message to a discord channel when a certain event occurs
# Author: Nash Sauter
import discord
from discord.ext import commands, bridge
import os
from Quote2Image import Convert, ImgObject
import random
from datetime import datetime
import dotenv

dotenv.load_dotenv()

BOT_TOKEN = str(os.getenv("DISCORD_BOT_KEY"))

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

activity = discord.Activity(name='Yoku no "Berlock"', type=discord.ActivityType.watching)
# client = discord.Client(intents = intents)

bot = bridge.Bot(command_prefix='$', intents = intents, activity = activity)

embed = ""

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.respond("get owned (command not recognized)")

@bot.slash_command(name = "confession", description = "Spill your deepest secrets")
async def confession(ctx, message):
    channel = bot.get_channel(1074944168843034704)
    date_time = datetime.now()
    await channel.send(f"**Confession at {date_time}**\n> {message}")

@bot.bridge_command(brief = "guess a number from 1 to 100")
async def guess100(ctx, guess:int):
    number = random.randint(1, 100)
    if guess == number:
        await ctx.respond(f"THE NUMBER WAS {number} BERLOCK BERLOCK BERLOCK!")
    else:
        await ctx.respond(f"the number was {number}, get berlocked")

@bot.command(brief = "pong")
async def ping(ctx):
    emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
    await ctx.message.add_reaction(emoji)
    await ctx.respond("Pong")

@bot.bridge_command(brief = "Generates an anonymous quote")
async def quote(ctx, quote_input):
    bg=ImgObject(image="white.jpg", brightness=100, blur=2)
    img=Convert(
        quote=quote_input,
        author="Anonymous Blighter",
        fg=(21, 21, 21),
        bg=bg,
        font_size=40,
        font_type="Raleway-Bold.ttf",
        watermark_text="",
        width=512,
        height=512)
    # return content
    img.save("quote.png")
    emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
    await ctx.message.add_reaction(emoji)
    await ctx.respond(file=discord.File('quote.png'))

@bot.message_command(name="Turn into a quote")
async def quotify(ctx, message: discord.Message):
    bg=ImgObject(image="white.jpg", brightness=100, blur=2)
    img=Convert(
        quote=f'"{message.content}"',
        author=message.author.name,
        fg=(21, 21, 21),
        bg=bg,
        font_size=40,
        font_type="Raleway-Bold.ttf",
        watermark_text="",
        width=512,
        height=512)
    # return content
    img.save("quote.png")
    await ctx.respond(file=discord.File('quote.png'))

bot.load_extension('cogs.memes')
bot.load_extension('cogs.gpt')

bot.run(BOT_TOKEN)
