import discord
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the token from the environment variable
token = os.getenv('TOKEN')

# Set the Intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Console log when the bot is ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Respond to the message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Run the bot
client.run(token)