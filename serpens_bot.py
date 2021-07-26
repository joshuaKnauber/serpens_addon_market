import discord
import pathlib
import random
import json
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
open_entries = {}


client = discord.Client()
@client.event
async def on_ready():
    print('Connected to Discord!')


def random_emoji():
    emojis = ["baseball", "dog", "cat", "hamster", "mouse", "rabbit", "fox", "bear", "dolphin", "gorilla", "ox", "dragon", "apple", "egg", "cooking", "hamburger", "pizza", "cake", "spoon", "basketball", "yo_yo", "drum", "red_car", "tram", "minidisc", "battery", "pig_nose"]
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

        if not user_id in open_entries:
            if message.content.lower() in ["addon", "a"]:
                open_entries[user_id] = {"type": "addon", "json": ""}
                await message.channel.send("<@" + str(message.author.id) + "> You want to upload an Addon! Cool! Just send me the message you got in serpens and paste it in here! You can type **Cancel** at any time to stop your upload process!")
            elif message.content.lower() in ["snippet", "s"]:
                open_entries[user_id] = {"type": "snippet"}
                await message.channel.send("<@" + str(message.author.id) + "> You want to upload a Snippet! Awesome! Just send me the json file, your zip file or a download link! You can type **Cancel** at any time to stop your upload process!")
            elif message.content.lower() in ["package", "p"]:
                open_entries[user_id] = {"type": "package"}
                await message.channel.send("<@" + str(message.author.id) + "> You want to upload a Package! idk what happens next pls send help! You can type **Cancel** at any time to stop your upload process!")
            else:
                await message.channel.send("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n<@" + str(message.author.id) + ">" + random_emoji() + " Hey, I don't have a conversation with you yet, just type:\n\n- **Addon** or **A** for uploading an addon\n- **Snippet** or **S** for uploading a snippet\n- **Package** or **P** for uploading a package")
        elif message.content.lower() == "cancel":
            open_entries.pop(user_id)
            await message.channel.send("<@" + str(message.author.id) + "> I canceled your upload! Feel free to try again at any time!")
        else:
            if open_entries[user_id]["type"] == "addon":
                if not open_entries[user_id]["json"]:
                    if is_valid_json(message.content):
                        open_entries[user_id]["json"] = json.loads(message.content)
                        if open_entries[user_id]["json"]["external"]:
                            if open_entries[user_id]["json"]["blend"]:
                                await message.channel.send("<@" + str(message.author.id) + "> Send me your blend file next!")
                            else:
                                await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your addon!")
                        else:
                            await message.channel.send("<@" + str(message.author.id) + "> Send me your addons zip file next!")
                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Please send me the message you copied in serpens first!")
                else:
                    if message.attachments:
                        addon_file = message.attachments[0]
                        file_name = addon_file.filename
                        if not open_entries[user_id]["json"]["external"] and not open_entries[user_id]["json"]["url"]:
                            if ".zip" in file_name:
                                open_entries[user_id]["json"]["url"] = save_file(addon_file)
                                if open_entries[user_id]["json"]["blend"]:
                                    await message.channel.send("<@" + str(message.author.id) + "> Send me your blend file next!")
                                else:
                                    await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your addon!")
                            else:
                                await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again!")
                        elif open_entries[user_id]["json"]["blend"]:
                            if ".blend" in file_name:
                                open_entries[user_id]["json"]["blend_url"] = save_file(addon_file)
                                await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your addon and blend file!")
                            else:
                                await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again!")
                        else:
                            await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again!")

                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again!")


        await message.delete()
        print(open_entries)
        # os.system("git add -A")
        # os.system("git commit -m\"Serverlog\"")
        # os.system("git pull")
        # os.system("git push")


client.run(TOKEN)

