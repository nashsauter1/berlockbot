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
        await ctx.respond("A dude who's an athlete, hot and everyone thinks he actually gets lots of pussy, but he's actually chill, kinda vibes, really vibey when stoned and can't get no pussy")

    @commands.command()
    async def girlsbelike(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.respond("Girls be like: we hate all men so we turn lesbian.\nBoys be like: uno reverse! *turns gay*\nGirls: shocked pikachu face\nSperm trying to get into eachother: confused stonks\nGoku: has sex with Wednesday\nWednesday: prenancy 100\nMe: only in Ohio!")

    @commands.command()
    async def indie(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.respond("imagine how much happier the world would be if more people chucked on a comfy fit (i personally like to go for the granola dad look), grabbed an iced oat latte and went to watch the sunset with their fav indie tunes blasting in the background.")

    @commands.command()
    async def normal(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.respond("is there still room for normal guys in society? i’m not a skater, alt boy, indie, jock, artist,… i’m just….. normal …i wear baseball hats… i wear hoodies … just a normal guy. And somehow i feel like i just…, don’t belong")

    @commands.command()
    async def O(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.respond("NGUYEN!")

    @commands.command()
    async def statement(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.respond('What the fuck, why the fuck, and as for who the fuck it’s 100% Alice Sauter"')

    @commands.command()
    async def cannibal(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.respond('```"Yes! It’ll be a meal full of delicious cruelty and greed" -Big Money\'s Redemption#6969```')

    @commands.command()
    async def sirens(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.respond('```"what\'s with the sirens? Is that world\'s end?  I want to be the mahatma of that siren voice, tell me how I should go about being a better person. What else can we do besides eating her?" -ExPeri3nce#0034```')

    @commands.command()
    async def pinklemonade(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.respond(':yum:yummy!:yum:')

    @commands.command()
    async def riichi(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.respond("Look at this absolute fucking legend sitting in front of me. This motherfucker, this smug mother fucker right here knows exact;y what I/I'm going for. He knows I'm in fucking tenpai for a dealer baiman, and you know what he does? He riichi. He doesn't even riichi a good wait mind you, no no no, mister can't afford throwing his precious red five to improve his wait a bit. No, he slams down his balls the size of grapefruits on the table and riichi this fucking KANCHAN. And you know what happens ? Of course you do. 'TSUMO, aaah yatto kita'. Ippatsu. He doesn't even look at me. He just proceeds with the game, because for him this is just natural. While I wonder where everything went wrong. ' What was I supposed to do?'. Look at my pond, look at it. I'm overdosing harder then a drug addict on luck, yet I'm not the one who wins/ I'm the one that gets to look like an utter buffoon. A pawn following what mahjong tells him to go for, as a joke. He even fed me all of them. A calculated risk, for he knew, he new that I'd fall for it. Calling them all one by one like a maniac, merely letting myself be taken by the flow, while he is harnessing it. The game was over before it even began. While he kept playing like usual, I was possessed by paranoia, doubting everything, lost in the dark, not knowing what I should even believe in, if there's even any hope for players like me. That's when I realized, mahjong isn't a game. It's a play. A cruel Theatre, as we're led to believe everyone hold the same role. But it's wrong. There are those the tiles will be kind to. They'll give them hard times once in a while, but they are undoubtedly love by them. To make up for that love they need to torment the other bunch. That's where I fit the bill. I'm comic relief, the guy at the table that everyone gets a good laugh out of. In a sense I'm needed. But I didn't ask for this. i just wanted to play mahjong, wanted to believe I, too, could, maybe, be loved.")

    @commands.command()
    async def opera(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.respond("Ok nobody cares. I'm 16 and I like to listen to everything from jazz to flamenco to cuban music of all tipes to peruvian guitar music to mongol throat singing and country and mariachis and some old italian songs and military anthems from Spain and Italy and some old catalan music and very old russian tunes with acordeon and argentinian and uruguayan guitar music amd boleros and all kind of stuff. But do I feel the need to come here and tell the world how classy I am? No. Do you know why? Cause it doesn't matter and nobody cares.")
        await ctx.respond("No hate.")

    @commands.command()
    async def mozart(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.respond("It utterly vexes me how Mozart is still put into the same tier as Beethoven/Bach when his magnum opus was partly ghostwritten by Sussmayr. Frankly it pisses me off to a degree that Mozart is still put up on a pedestal and treated as this genius sent down by God when he put out a FRACTION of what Bach put out and also didn’t innovate for shit. He deserves to be the punching bag of the classical music community. Liking Mozart is like liking club music. It sounds like a decent tune at a surface level, but it’s not meant to be listened to in a vacuum. It’s meant to supplement something that actually has substance. The fact that he only wrote 2 pieces in minor scale should tell you everything you need to know about it this guy.")

    @commands.command()
    async def runescape(self, ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name='ohmydog')
        await ctx.message.add_reaction(emoji)
        await ctx.respond("I used to play only 30 hours of osrs a week until I took reddits advice. You all told me to go to a therapist cause I played too much. Well I went to a therapist and he didn't say I played too much! He diagnosed me with ADHD. Now I'm on 40 mg of Adderall a day and haven't missed a tick in at least 2 years. I may now play around 80 hours a week, but its all good cause I can focus the whole time. I do have an appointment to see a specialist about wrist and hand pain, but I'm not worried because I'm sure the pain is just due to my ADHD. Anyways thank you reddit. I can't put my appreciation into words. Without you I never would've realized my goal of 200 mil all skills")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Memes(bot)) # add the cog to the bot
