#is this discord.py?
import discord

client = discord.Client()

@client.event
async def on_message(message):
    print(message.content)
    if message.content.find("woof.woof") != -1:
        await message.channel.send("woof woof")

client.run("NzAxNDE2ODM4NzU5NzEwODEw.XpxP1g.P9sieWx_TGclIs4iBIFDOoAwgXw")