import discord
from discord.ext import commands, bridge
import wavelink

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def connect_nodes(self):
      """Connect to our Lavalink nodes."""
      await self.bot.wait_until_ready() # wait until the bot is ready

      await wavelink.NodePool.create_node(
        bot=self.bot,
        host='0.0.0.0',
        port=2333,
        password='berlock'
      ) # create a nodes

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(self.connect_nodes())
        print("Cog: Music Loaded")

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node):
        print(f"Node {node.identifier} is ready")


    @bridge.bridge_command(name="play")
    async def play(self, ctx, search: str):
      vc = ctx.voice_client # define our voice client

      if not vc: # check if the bot is not in a voice channel
        vc = await ctx.author.voice.channel.connect(cls=wavelink.Player) # connect to the voice channel
      if ctx.author.voice.channel.id != vc.channel.id: # check if the bot is not in the voice channel
        return await ctx.respond("You must be in the same voice channel as the bot.") # return an error message

      song = await wavelink.YouTubeTrack.search(query=search, return_first=True) # search for the song
      if not song: # check if the song is not found
        return await ctx.respond("No song found.") # return an error message

      await vc.play(song) # play the song
      await ctx.respond(f"Now playing: `{vc.source.title}`") # return a message

    @bridge.bridge_command(name="stop")
    async def stop(self, ctx):
        vc = ctx.voice_client
        await vc.disconnect()
        await ctx.respond("Player has stopped")

    @commands.Cog.listener()
    async def on_ready(self):
        await self.connect_nodes() # connect to the server

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Music(bot)) # add the cog to the bot
