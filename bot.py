import discord
import pathlib
import json
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()
@client.event
async def on_ready():
    print('Connected to Discord!')


def has_open_entry(user_id):
    with open("./open_entries.json") as open_entries:
        open_entries = json.load(open_entries)
        for entry in open_entries["entries"]:
            if entry["user"] == user_id:
                return True
    return False

def find_open_entry(user_id):
    with open("./open_entries.json") as open_entries:
        open_entries = json.load(open_entries)
        for entry in open_entries["entries"]:
            if entry["user"] == user_id:
                return entry
    return None

def remove_open_entry(user_id):
    with open("./open_entries.json", "r+") as open_entries:
        open_entries_json = json.load(open_entries)
        for x, entry in enumerate(open_entries_json["entries"]):
            if entry["user"] == user_id:
                open_entries_json["entries"].pop(x)

        open_entries.seek(0)
        open_entries.write(json.dumps(open_entries_json, skipkeys=True, indent=4))
        open_entries.truncate()

def add_open_entry(entry_json):
    with open("./open_entries.json", "r+") as open_entries:
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

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == 766772440222138368:
        user_id = message.author.id
        # if message is a file
        if message.attachments:
            addon_file = message.attachments[0]
            # if user has open entry
            if has_open_entry(user_id):
                # if file is python file
                if addon_file.filename.split(".")[-1] == "py":
                    # if exists in addons.json
                    if addon_exists(user_id, find_open_entry(user_id)["name"]):
                        # delete old data
                        if os.path.exists(os.path.join(os.path.dirname(os.path.realpath(__file__)), "addons", find_addon(user_id, find_open_entry(user_id)["name"])["url"])):
                            os.system("rm addons/" + find_addon(user_id, find_open_entry(user_id)["name"])["url"])
                            #os.system("rm addons/" + find_open_entry(user_id)["url"])

                        remove_addon(user_id, find_open_entry(user_id)["name"])
                        await message.channel.send("<@" + str(message.author.id) + "> Updated your old addon!")
                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Added your addon to marketplace!")

                    # save file
                    await addon_file.save("./addons/" + addon_file.filename.split(".")[0] + str(user_id) + ".py")

                    # put open entry and reference to file in addons.json
                    new_entry = find_open_entry(user_id)
                    new_entry["url"] = addon_file.filename.split(".")[0] + str(user_id) + ".py"
                    add_addon(new_entry)

                    # remove open entry
                    remove_open_entry(user_id)

                    os.system("git add -A")
                    os.system("git commit -m\"Updated or added an addon\"")
                    os.system("git push")

                else:
                     # "post a python file"
                    await message.channel.send("<@" + str(message.author.id) + "> Please post a python file!")
            else:
                # "post your message first"
                await message.channel.send("<@" + str(message.author.id) + "> Please post the message you got in blender first!")

        else:
            # if is valid json
            if is_valid_json(message.content):
                json_message = json.loads(message.content)
                json_message["user"] = user_id
                # if using url
                if json_message["url"]:
                    # if exists in addons.json
                    if addon_exists(user_id, json_message["name"]):
                        # overwrite old data with new data
                        remove_addon(user_id, json_message["name"])
                        await message.channel.send("<@" + str(message.author.id) + "> Updated your addon :+1:")
                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Added your addon :+1:")

                    # add new data to file
                    add_addon(json_message)

                    os.system("git add -A")
                    os.system("git commit -m\"Updated or added an addon\"")
                    os.system("git push")
                else:
                    # if has openentry
                    if has_open_entry(user_id):
                        # delete old entry
                        await message.channel.send("<@" + str(message.author.id) + "> Removed your old entry")
                        remove_open_entry(user_id)
                    # add new entry
                    add_open_entry(json_message)
                    await message.channel.send("<@" + str(message.author.id) + "> Send your file next!")

            else:
                # "please try again"
                await message.channel.send("<@" + str(message.author.id) + "> Something went wrong :pensive: Please try again!")

        await message.delete()

client.run(TOKEN)

