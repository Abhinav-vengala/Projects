import discord
import os
import random

TOKEN = 'MTAxNDU4MjQ0MTQxMjkzNTc0MQ.GPVWEN.w4rHsZYgzrkQHK6V8U9gw9p3Bji9zkHe_MuNXE'

my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username} : {user_message} ({channel})')

    if message.author == client.user:
        return
    if message.channel.name == 'general':
      if user_message.lower() == 'hello':
          await message.channel.send(f'Hello {username}!')
          return
      elif user_message.lower() == 'bye':
          await message.channel.send(f'See you later {username}!')
          return
      elif user_message.lower() == 'hi':
          await message.channel.send(f'Hi {username}!')
          return
      elif user_message.lower() == 'random':
          await message.channel.send('This is an random message!')
          return



client.run(my_secret) 
