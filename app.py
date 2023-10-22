# bot.py
import os
import logging
import discord
import random

logging.basicConfig(level=logging.DEBUG)

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.reactions = True
intents.guild_messages = True
intents.guild_reactions = True
intents.dm_messages = True



class MyClient(discord.Client):
    async def on_ready(self):
        for guild in self.guilds:

            print(
                f'{client.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
            )
            members = '\n - '.join([member.name for member in guild.members])
            print(f'Guild Members:\n - {members}')

    async def on_message(self, message: discord.Message):
        # don't respond to ourselves
        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]
        print(message)
        print(message.content)
        # if message.author.id == self.user.id:
        if message.content == 'show':
            print(message)
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)

# client = discord.Client(intents=intents)

# @client.event
# async def on_ready():


client = MyClient(intents=intents)

print(TOKEN)
client.run(TOKEN, reconnect=True)