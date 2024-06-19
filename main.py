import discord 

bot = discord.Bot()

# Prints in terminal as soon as bot is active
@bot.event 
async def on_ready():
  print(f"We have logged in as {bot.user}")
  

# ID's for the server we are testing on
testingServers = []

# Create a slash command (hello world)
@bot.slash_command(guild_ids=testingServers, name="work", description="Checks to see if I am online")
async def work(ctx):
  await ctx.respond(f"I am working! \n\nLatency: {bot.latency*1000}ms")