import discord
import json
import os

TOKEN = "NzY2NzUyMTU1NzMwMTgyMTg0.X4n7lw.gHoZCW5b7-Er8zF3dlhi10L29J4"
client = discord.Client()
@client.event
async def on_ready():
    print('Connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel == 766757128152416297:
        message.channel.send("Hi")

client.run(TOKEN)

