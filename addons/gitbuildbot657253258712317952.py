# bot.py
import os
import discord

TOKEN = "NzEzNDYyOTY1NjQyMTk5MTAx.XsgeMg.iNNrukr8Adx_zdAgVhZxDZv7eGs"

client = discord.Client()


@client.event
async def on_ready():
    print('Connected to Discord!')


async def sendText(text):
    channel = client.get_channel(713459891569950790)
    os.system("wget --auth-no-challenge --user=finnknauber --password=0c3ca18d69c22571110903fe6acab50f400dd515 --output-document=visual_scripting_addon_alpha.zip https://github.com/joshuaKnauber/blender_visual_scripting_addon/archive/master.zip")
    fileobject = discord.File(r"visual_scripting_addon_alpha.zip")
    await channel.send(content=text, file=fileobject)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if str(message.channel) == "build-messages":
        content = message.embeds[0].title
        content = content.split(":")[1]
        content = content.split("]")[0]
        if content == "master":
            content = message.embeds[0].description
            content = content.split("\n")

            fullContent = "Changes:\n"
            for line in content:
                line = line.split(")")
                line = line[1].split("-")[0].strip()
                if not "Merge branch" in line and not "internal" in line:
                    fullContent+= "- " + line + "\n"
            if fullContent != "Changes:\n":
                await sendText(fullContent)


client.run(TOKEN)
