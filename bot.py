import discord
import pathlib
import random
import json
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()
@client.event
async def on_ready():
    print('Connected to Discord!')


def random_emoji():
    emojis = ["baseball", "dog", "cat", "hamster", "mouse", "rabbit", "fox", "bear", "dolphin", "gorilla", "ox", "dragon", "apple", "egg", "cooking", "hamburger", "pizza", "cake", "spoon", "basketball", "yo_yo", "drum", "red_car", "tram", "minidisc", "battery"]
    return ":" + emojis[random.randint(0, len(emojis)-1)] + ":"

def has_open_entry(user_id):
    with open("./json_data.json") as open_entries:
        open_entries = json.load(open_entries)
        for entry in open_entries["entries"]:
            if entry["user"] == user_id:
                return True
    return False

def find_open_entry(user_id):
    with open("./json_data.json") as open_entries:
        open_entries = json.load(open_entries)
        for entry in open_entries["entries"]:
            if entry["user"] == user_id:
                return entry
    return None

def remove_open_entry(user_id):
    with open("./json_data.json", "r+") as open_entries:
        open_entries_json = json.load(open_entries)
        for x, entry in enumerate(open_entries_json["entries"]):
            if entry["user"] == user_id:
                open_entries_json["entries"].pop(x)

        open_entries.seek(0)
        open_entries.write(json.dumps(open_entries_json, skipkeys=True, indent=4))
        open_entries.truncate()

def add_open_entry(entry_json):
    with open("./json_data.json", "r+") as open_entries:
        open_entries_json = json.load(open_entries)
        open_entries_json["entries"].append(entry_json)
        open_entries.seek(0)
        open_entries.write(json.dumps(open_entries_json, skipkeys=True, indent=4))
        open_entries.truncate()

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

    # if message in addon-market
    if message.channel.id in [767853772562366514, 768053288989360128]:
        user_id = message.author.id
        # if message is a file
        if message.attachments:
            addon_file = message.attachments[0]
            file_name = addon_file.filename
            # if has open entry
            if has_open_entry(user_id):
                open_entry = find_open_entry(user_id)
                using_blender_file = open_entry["blend"]
                # if is python file
                if addon_file.filename.split(".")[-1] == "py":
                    if using_blender_file:
                        remove_open_entry(user_id)
                        open_entry["url"] = await save_file(addon_file)
                        add_open_entry(open_entry)
                        await message.channel.send("<@" + str(message.author.id) + "> Post your blender file next " + random_emoji())
                    else:
                        # put open entry and reference to file in addons.json
                        open_entry["url"] = await save_file(addon_file)
                        if addon_exists(user_id, open_entry["name"]):
                            remove_addon(user_id, open_entry["name"])
                            remove_open_entry(user_id)
                            add_addon(open_entry)
                            await message.channel.send("<@" + str(message.author.id) + "> Updated your old addon " + random_emoji())
                        else:
                            remove_open_entry(user_id)
                            add_addon(open_entry)
                            await message.channel.send("<@" + str(message.author.id) + "> Added your addon to the marketplace " + random_emoji())


                # elif is zip file
                elif addon_file.filename.split(".")[-1] == "zip":
                    if using_blender_file:
                        remove_open_entry(user_id)
                        open_entry["url"] = await save_file(addon_file)
                        add_open_entry(open_entry)
                        await message.channel.send("<@" + str(message.author.id) + "> Post your blender file next " + random_emoji())
                    else:
                        # put open entry and reference to file in addons.json
                        open_entry["url"] = await save_file(addon_file)
                        if addon_exists(user_id, open_entry["name"]):
                            remove_addon(user_id, open_entry["name"])
                            remove_open_entry(user_id)
                            add_addon(open_entry)
                            await message.channel.send("<@" + str(message.author.id) + "> Updated your old addon " + random_emoji())
                        else:
                            remove_open_entry(user_id)
                            add_addon(open_entry)
                            await message.channel.send("<@" + str(message.author.id) + "> Added your addon to the marketplace " + random_emoji())


                # elif is blender file
                elif addon_file.filename.split(".")[-1] == "blend":
                    if using_blender_file:
                        if open_entry["url"]:
                            remove_open_entry(user_id)
                            open_entry["blend_url"] = await save_file(addon_file)
                            add_addon(open_entry)
                            await message.channel.send("<@" + str(message.author.id) + "> Added your addon and blend file to the marketplace " + random_emoji())
                        else:
                            await message.channel.send("<@" + str(message.author.id) + "> Please post your python file first! " + random_emoji())
                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Please select the blender file option before uploading " + random_emoji())
                # else
                else:
                    await message.channel.send("<@" + str(message.author.id) + "> Please send a .py, .zip or .blend file! " + random_emoji())
            # else
            else:
                # "post your message first"
                await message.channel.send("<@" + str(message.author.id) + "> Please post the message you got in blender first! " + random_emoji())



        # if message is not a file
        else:
            # if is valid json
            if is_valid_json(message.content):
                json_message = json.loads(message.content)
                json_message["user"] = user_id
                # if using url
                if not "external" in json_message:
                    await message.channel.send("<@" + str(message.author.id) + "> Please use the newest version of the serpens addon! " + random_emoji())

                else:
                    if json_message["external"]:
                        using_blender_file = json_message["blend"]
                        # if exists in addons.json
                        if using_blender_file:
                            if addon_exists(user_id, json_message["name"]):
                                remove_addon(user_id, json_message["name"])

                            # if has openentry
                            if has_open_entry(user_id):
                                # delete old entry
                                await message.channel.send("<@" + str(message.author.id) + "> Removed your old entry " + random_emoji())
                                remove_open_entry(user_id)
                            # add new entry
                            add_open_entry(json_message)
                            await message.channel.send("<@" + str(message.author.id) + "> Send your blender file next! " + random_emoji())

                        else:
                            if addon_exists(user_id, json_message["name"]):
                                remove_addon(user_id, json_message["name"])

                                await message.channel.send("<@" + str(message.author.id) + "> Updated your addon! " + random_emoji())
                            else:
                                await message.channel.send("<@" + str(message.author.id) + "> Added your addon to the marketplace! " + random_emoji())

                            # add new data to file
                            add_addon(json_message)

                    else:
                        # if has openentry
                        if has_open_entry(user_id):
                            # delete old entry
                            await message.channel.send("<@" + str(message.author.id) + "> Removed your old entry " + random_emoji())
                            remove_open_entry(user_id)
                        # add new entry
                        add_open_entry(json_message)
                        await message.channel.send("<@" + str(message.author.id) + "> Send your file next! " + random_emoji())


            # remove addons
            elif message.content.split(" ")[0] == "remove":
                # if the addon exists
                if addon_exists(user_id, message.content[7:]):
                    # remove it from the json file
                    remove_addon(user_id, message.content[7:])
                    # send confirmation
                    await message.channel.send("<@" + str(message.author.id) + "> Removed your Addon! " + random_emoji())

                # addon doesn't exist
                else:
                    await message.channel.send("<@" + str(message.author.id) + "> This addon does not exist " + random_emoji())

            # something went wrong
            else:
                # "please try again"
                await message.channel.send("<@" + str(message.author.id) + "> Something went wrong :pensive: Please try again!")

        await message.delete()
        os.system("git add -A")
        os.system("git commit -m\"Serverlog\"")
        os.system("git pull")
        os.system("git push")


client.run(TOKEN)

