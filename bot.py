import discord
import pathlib
import random
import json
import os

TOKEN = "NzY2NzUyMTU1NzMwMTgyMTg0.X4n7lw.bBn6jpQooqaISDUPtgEQhXv7hrU"

client = discord.Client()
@client.event
async def on_ready():
    print('Connected to Discord!')


def random_emoji():
    emojis = ["baseball", "dog", "cat", "hamster", "mouse", "rabbit", "fox", "bear", "dolphin", "gorilla", "ox", "dragon", "apple", "egg", "cooking", "hamburger", "pizza", "cake", "spoon", "basketball", "yo_yo", "drum", "red_car", "tram", "minidisc", "battery"]
    return ":" + emojis[random.randint(0, len(emojis)-1)] + ":"

def addon_exists(user_id, name):
    with open("./addons.json") as addons:
        addons = json.load(addons)
        for entry in addons["addons"]:
            if entry["user"] == user_id and entry["name"] == name:
                return True
    return False

def remove_addon(user_id, name):
    with open("./addons.json", "r+") as addons:
        addons_json = json.load(addons)
        for x, entry in enumerate(addons_json["addons"]):
            if entry["user"] == user_id and entry["name"] == name:
                addons_json["addons"].pop(x)
        addons.seek(0)
        addons.write(json.dumps(addons_json, skipkeys=True, indent=4))
        addons.truncate()

def add_addon(addon_json):
    with open("./addons.json", "r+") as addons:
        addons_json = json.load(addons)
        addons_json["addons"].append(addon_json)
        addons.seek(0)
        addons.write(json.dumps(addons_json, skipkeys=True, indent=4))
        addons.truncate()

def find_addon(user_id, name):
    with open("./addons.json") as addons:
        addons_json = json.load(addons)
        for addon in addons_json["addons"]:
            if addon["user"] == user_id and addon["name"] == name:
                return addon
    return None

def is_valid_json(json_str):
    valid = False
    try:
        json.loads(json_str)
        valid = True
    except json.JSONDecodeError:
        pass

    return valid

async def save_file(save_file):
    file_name = save_file.filename
    channel = client.get_channel(785132940278366260)

    await save_file.save(file_name)
    fileobject = discord.File(file_name)
    message = await channel.send(file=fileobject)

    os.system("rm " + file_name)

    return message.attachments[0].url

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if message in addon-market or commands
    if message.channel.id in [767853772562366514, 768053288989360128]:
        user_id = message.author.id
        # if message is a file
        if message.attachments:
            addon_file = message.attachments[0]
            file_name = addon_file.filename

        # if message is not a file
        else:
            pass

        await message.channel.send("<@" + str(message.author.id) + "> Done! " + random_emoji())
        await message.delete()
        os.system("git add -A")
        os.system("git commit -m\"Serverlog\"")
        os.system("git pull")
        os.system("git push")


client.run(TOKEN)

