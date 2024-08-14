import os
import discord
import time
from chunkysnotded import chunkysnotded
client = discord.Client()
prefix = '!'
player = {'a':[0, False, False]}
adminFalse = f'You need to be an administrator to use this command'

@client.event
async def on_member_join(member):
  print(member.name)
  player[member.name] = [0, False, False]
@client.event
async def on_ready():
  print('------')
  print(client.user.name)
  print(client.user.id)
  print('------')
  for i in client.guilds:
    if i.name == 'deeeeeeeeeeeeeeeeeeeeeeeeeeev' or i.name == 'Game Jam' or i.name == 'let\'s get carpal tunnel':
      for member in i.members:
        player[member.name] = [0, False, False]
  
@client.event
async def on_message(message):
  global prefix, player

  if message.content.startswith(prefix + 'credit') and message.author.guild_permissions.administrator:
    a = message.content.split()
    b = int(message.content.split()[-1])
    if len(a) >= 3 and message.content[len(message.content)-1].isdigit():
        if message.content[len(message.content)-2] == '-':
          a1 = str(message.content[8:len(message.content)-3])
          a2 = int(message.content[len(message.content)-2:])
        else:
          a2 = int(message.content[len(message.content)-1])
          a1 = str(message.content[8:len(message.content)-2])
        if a1 in player.keys():
            player[a1][0] += b
        msg = f'{a1} has recieved +{b} credits!'
        await message.channel.send(msg)
    elif message.content.startswith(prefix + 'credit') and message.author.guild_permissions.administrator == False:
        await message.channel.send(adminFalse)
    else:
        msg = f'Invalid Syntax. Please try saying \'(prefix)credit (name) (#) instead.'
        await message.channel.send(msg)

  if message.content.startswith(prefix + 'ccredits'):
      a = message.content.split()
      if len(a) > 1:
          a1 = message.content[10:]
      else:
          a1 = message.author.name
      if a1 in player.keys():
          msg = f'{a1} has {player[a1][0]} credits.'
          await message.channel.send(msg)
      else:
          msg = f'{a1} has 0 credits.'
          await message.channel.send(msg)

  if message.content.startswith(prefix + 'change') and message.author.guild_permissions.administrator:
    prefix = message.content.split()[1]
    msg = f'Prefix set to {prefix}'
    await message.channel.send(msg)

  e = message.mentions
  if e:
    for i in e:
      if i.id == int(os.environ.get('IDOFCLIENTE')):
        msg = f'''
        Hey {message.author.name}!
        Here is a list of all of the usable commands at the moment. For more support dm Ballistiq#1992 on discord.
        [!credit (name) (#): Award credits to a user (Administrator needed)]
        [!ccredits (name(optional)): Checks user's credits, if no name, it will check author's credits]
        [!clear (#): Clears messages (Administrator needed)]
        '''
        await message.author.send(msg)

  if message.content.startswith(prefix + 'help'):
    msg = 'Ping Me in this server or in Dms for the commands list.'
    await message.channel.send(msg)

  if message.content.startswith(prefix + 'clear'):
    if len(message.content.split()) > 1:
      a1 = int(message.content.split()[1])
      variable1 = []
      a1 += 1
      variable1 = await message.channel.history(limit = a1).flatten()
      await message.channel.delete_messages(variable1)
      msg = f'{a1 - 1} messages deleted.'
      await message.channel.send(msg)
      time.sleep(2.0)
      variable1 = await message.channel.history(limit = 1).flatten()
      await message.channel.delete_messages(variable1)

chunkysnotded()
token_get = os.environ.get("ROBOTOKEN")
client.run(token_get)