import discord
from discord.ext import commands, bridge
import wavelink

class CustomPlayer(wavelink.Player):
    def __init__(self):
        super().__init__()
        self.queue = wavelink.Queue()

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

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player, track, reason):
        if not player.queue.is_empty:
            next_track = player.queue.get()
            await player.play(next_track)

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

        if vc.is_playing():
            await ctx.respond(f"Queued: `{song.title}`") # return a message
            await vc.queue.put(item=song)
        else:
            await vc.play(song) # play the song
            await ctx.respond(f"Now playing: `{vc.source.title}`") # return a message

    @bridge.bridge_command(name="stop")
    async def stop(self, ctx):
        vc = ctx.voice_client
        await vc.disconnect()
        await ctx.respond("Player has stopped")
    
    @bridge.bridge_command(name="skip")
    async def skip(self, ctx):
        vc = ctx.voice_client
        if vc:
            if not vc.is_playing():
                return await ctx.send("Nothing is playing.")
            if vc.queue.is_empty:
                return await vc.stop()

            await vc.seek(vc.track.length * 1000)
            if vc.is_paused():
                await vc.resume()

    @commands.Cog.listener()
    async def on_ready(self):
        await self.connect_nodes() # connect to the server

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Music(bot)) # add the cog to the bot
