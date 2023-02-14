# Discord bot that sends a message to a discord channel when a certain event occurs
# Author: Nash Sauter
import discord
from discord.ext import commands
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

bot = commands.Bot(command_prefix='$', intents = intents, activity = activity)
embed = ""

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("get owned (command not recognized)")


# Simple Commands
@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("berlock")

@bot.slash_command(name = "confession", description = "Spill your deepest secrets")
async def confession(ctx, message):
    channel = bot.get_channel(1074944168843034704)
    date_time = datetime.now()
    await channel.send(f"**Confession at {date_time}**\n> {message}")

@bot.command(brief = "guess a number from 1 to 100")
async def guess100(ctx, guess:int):
    number = random.randint(1, 100)
    if guess == number:
        await ctx.send(f"THE NUMBER WAS {number} BERLOCK BERLOCK BERLOCK!")
    else:
        await ctx.send(f"the number was {number}, get berlocked")

@bot.command(brief = "pong")
async def ping(ctx):
    emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
    await ctx.message.add_reaction(emoji)
    await ctx.channel.send("Pong")

# GPT
import berlock_gpt

@bot.command(brief = "missAInthrope proverbs")
async def proverb(ctx):
    alice_answer = berlock_gpt.proverbGPT().strip()
    embed = discord.Embed(title="Blight AI",
                          url="https://zombo.com",
                      colour=0x00fcff)
    embed.set_author(name="Berlock Bot",
                     icon_url="https://images-ext-2.discordapp.net/external/XaZD0LjdRFtLqJKRHD96hbM3Yrxo0Nr2bQrkz2yN7Uk/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/1027808278551461988/d9ce0c74f3aa9fb61e44fb9b186dd9bd.png")
    embed.add_field(name="Proverb Generator",
                    value=f"```{alice_answer} \n\n-missanthrope#0429```")
    emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
    await ctx.message.add_reaction(emoji)
    await ctx.channel.send(embed = embed)

@bot.command(brief = "Nash AI Q&A")
async def asknash(ctx, question):
    nash_answer = berlock_gpt.asknashGPT(question).strip()
    embed = discord.Embed(title="Blight AI",
                          url="https://zombo.com",
                      colour=0x2b39e5)
    embed.set_author(name="Berlock Bot",
                     icon_url="https://images-ext-2.discordapp.net/external/XaZD0LjdRFtLqJKRHD96hbM3Yrxo0Nr2bQrkz2yN7Uk/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/1027808278551461988/d9ce0c74f3aa9fb61e44fb9b186dd9bd.png")
    embed.add_field(name="Nash AI Q&A",
                    value=f"```User: {question}\nNash: {nash_answer}```")
    emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
    await ctx.message.add_reaction(emoji)
    await ctx.channel.send(embed = embed)

@bot.command(brief = "Takes User ID and question as input")
async def askblight(ctx, blight, *, question):
    blight_answer = berlock_gpt.askblightGPT(blight, question).strip()
    embed = discord.Embed(title="Blight AI",
                          url="https://zombo.com",
                      colour=0x6ab1b3)
    embed.set_author(name="Berlock Bot",
                     icon_url="https://images-ext-2.discordapp.net/external/XaZD0LjdRFtLqJKRHD96hbM3Yrxo0Nr2bQrkz2yN7Uk/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/1027808278551461988/d9ce0c74f3aa9fb61e44fb9b186dd9bd.png")
    embed.add_field(name="Blight AI Q&A",
                    value=f"```User: {question}\n{blight}: {blight_answer}```")
    emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
    await ctx.message.add_reaction(emoji)
    await ctx.channel.send(embed = embed)

@bot.command(brief = "Generates an anonymous quote")
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
    await ctx.channel.send(file=discord.File('quote.png'))

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

@bot.command(brief = "Image version of proverb")
async def proverb_img(ctx):
    alice_answer = berlock_gpt.proverbGPT()
    bg=ImgObject(image="white.jpg", brightness=100, blur=2)
    img=Convert(
        quote=alice_answer,
        author="missanthrope#0429",
        fg=(21, 21, 21),
        bg=bg,
        font_size=34,
        font_type="Raleway-Bold.ttf",
        watermark_text="",
        width=512,
        height=512)
    # return content
    img.save("quote.png")
    emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
    await ctx.message.add_reaction(emoji)

    file = discord.File("quote.png", filename="quote.png")
    embed = discord.Embed(title="Blight AI",
                          url="https://zombo.com",
                      colour=0x85ed93)
    embed.set_author(name="Berlock Bot",
                     icon_url="https://images-ext-2.discordapp.net/external/XaZD0LjdRFtLqJKRHD96hbM3Yrxo0Nr2bQrkz2yN7Uk/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/1027808278551461988/d9ce0c74f3aa9fb61e44fb9b186dd9bd.png")
    embed.set_image(url="attachment://quote.png")
    embed.add_field(name="Proverb Generator", value = "")
    await ctx.channel.send(file = file, embed = embed)


@bot.command(brief = "Infographic generator based on a topic")
async def infographic(ctx, *, input_topic):
    tagline = berlock_gpt.infographicGPT(input_topic)
    berlock_gpt.infographic_image(tagline)
    emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
    await ctx.message.add_reaction(emoji)

    file = discord.File("infographic.png", filename="infographic.png")
    embed = discord.Embed(title="Blight AI",
                          url="https://zombo.com",
                      colour=0x85ed93)
    embed.set_author(name="Berlock Bot",
                     icon_url="https://images-ext-2.discordapp.net/external/XaZD0LjdRFtLqJKRHD96hbM3Yrxo0Nr2bQrkz2yN7Uk/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/1027808278551461988/d9ce0c74f3aa9fb61e44fb9b186dd9bd.png")
    embed.set_image(url="attachment://infographic.png")
    embed.add_field(name="Infographic Generator", value = "")
    await ctx.channel.send(file = file, embed = embed)


bot.load_extension('cogs.memes')

bot.run(BOT_TOKEN)
