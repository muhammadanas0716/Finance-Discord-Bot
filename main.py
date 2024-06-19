import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the token from the environment variable
token = os.getenv('TOKEN')

# Set the Intents
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Console log when the bot is ready
@bot.event
async def on_ready():
    print(f'We have logged in as {client.user}')


help = SlashCommandGroup(name="help", description="Help command", guild_ids=[1252923017022148679])



# Respond to the message
@help.command
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Run the bot
client.run(token)