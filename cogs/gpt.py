import discord
from discord.ext import commands
import berlock_gpt
from Quote2Image import Convert, ImgObject

class GPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief = "bye bye!") # we can also add application commands
    async def goodbye(self, ctx):
        await ctx.send('Berlock bye bye!')

    
    @commands.command(brief = "missAInthrope proverbs")
    async def proverb(self, ctx):
        alice_answer = berlock_gpt.proverbGPT().strip()
        embed = discord.Embed(title="Blight AI",
                              url="https://zombo.com",
                          colour=0x00fcff)
        embed.set_author(name="Berlock Bot",
                         icon_url="https://images-ext-2.discordapp.net/external/XaZD0LjdRFtLqJKRHD96hbM3Yrxo0Nr2bQrkz2yN7Uk/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/1027808278551461988/d9ce0c74f3aa9fb61e44fb9b186dd9bd.png")
        embed.add_field(name="Proverb Generator",
                        value=f"```{alice_answer} \n\n-missanthrope#0429```")
        emoji = discord.utils.get(self, ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.channel.send(embed = embed)

    @commands.command(brief = "Nash AI Q&A")
    async def asknash(self, ctx, question):
        nash_answer = berlock_gpt.asknashGPT(question).strip()
        embed = discord.Embed(title="Blight AI",
                              url="https://zombo.com",
                          colour=0x2b39e5)
        embed.set_author(name="Berlock Bot",
                         icon_url="https://images-ext-2.discordapp.net/external/XaZD0LjdRFtLqJKRHD96hbM3Yrxo0Nr2bQrkz2yN7Uk/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/1027808278551461988/d9ce0c74f3aa9fb61e44fb9b186dd9bd.png")
        embed.add_field(name="Nash AI Q&A",
                        value=f"```User: {question}\nNash: {nash_answer}```")
        emoji = discord.utils.get(self, ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.channel.send(embed = embed)

    @commands.command(brief = "Takes User ID and question as input")
    async def askblight(self, ctx, blight, *, question):
        blight_answer = berlock_gpt.askblightGPT(blight, question).strip()
        embed = discord.Embed(title="Blight AI",
                              url="https://zombo.com",
                          colour=0x6ab1b3)
        embed.set_author(name="Berlock Bot",
                         icon_url="https://images-ext-2.discordapp.net/external/XaZD0LjdRFtLqJKRHD96hbM3Yrxo0Nr2bQrkz2yN7Uk/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/1027808278551461988/d9ce0c74f3aa9fb61e44fb9b186dd9bd.png")
        embed.add_field(name="Blight AI Q&A",
                        value=f"```User: {question}\n{blight}: {blight_answer}```")
        emoji = discord.utils.get(self, ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.channel.send(embed = embed)

    @commands.command(brief = "Image version of proverb")
    async def proverb_img(self, ctx):
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
        emoji = discord.utils.get(self, ctx.guild.emojis, name='ohmydog')
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


    @commands.command(brief = "Infographic generator based on a topic")
    async def infographic(self, ctx, *, input_topic):
        tagline = berlock_gpt.infographicGPT(input_topic)
        berlock_gpt.infographic_image(tagline)
        emoji = discord.utils.get(self, ctx.guild.emojis, name='ohmydog')
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

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(GPT(bot)) # add the cog to the bot
