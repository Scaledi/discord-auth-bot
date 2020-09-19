# region: imports
import re
import discord # pip install discord.py
import os
import random
import string
import config

# endregion
# region:parsing

# endregion
# region: interaction with discord
client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    keys = []
    with open("keys.txt", "r") as keystxt:
        for line in keystxt.readlines():
            keys.append(line.rstrip('\n'))

    if message.author == client.user:
        return
    else:
        guild = message.guild
        rolename = discord.utils.get(guild.roles, id=config.role)
        msg = message.content
        try: # set message as key input
            iskey = keys.index(msg) # may trigger unused, as it is not refrenced in the code, however this is VERY importaint. this code may trigger a error, or now, allowing the exsept and else to run.
        except ValueError: # if its not a key
            await message.channel.send('**Error:** Not a valid key!')
        else: # if it is a key
            sucmessage = await message.channel.send('**Key Valid:** Role is being added, and key is now invalidated for future use.')
            keys.remove(str(msg))
            with open("keys.txt", 'w') as output:
                for row in keys:
                    output.write(str(row) + '\n')
            try:
                await message.author.add_roles(rolename, reason=None, atomic=True)
            except discord.errors.Forbidden:
                await sucmessage.delete()
                await message.channel.send("""**IMPORTAINT NOTE!!!** - ***THIS USER HAS NOT RECEIVED THEIR ROLE!!!!*** and, **the key IS NOW INVALID**. read about why this is at the link provided. 
https://github.com/Scaledi/discord-auth-bot/wiki/Why-is-key-invalid-without-granting-role%3F
*please manually grant their role*""")

client.run(config.token)
# endregion