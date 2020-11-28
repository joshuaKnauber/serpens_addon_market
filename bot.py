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

    if message.channel.id in [767853772562366514, 696821844975681550]:
        user_id = message.author.id
        # if message is a file
        if message.attachments:
            addon_file = message.attachments[0]
            # if user has open entry
            if has_open_entry(user_id):
                using_blender_file = find_open_entry(user_id)["blend"]
                # if file is python file
                if addon_file.filename.split(".")[-1] in ["py"]:
                    # if exists in addons.json
                    if addon_exists(user_id, find_open_entry(user_id)["name"]):
                        # delete old data
                        if os.path.exists(os.path.join(os.path.dirname(os.path.realpath(__file__)), "addons", find_addon(user_id, find_open_entry(user_id)["name"])["url"])):
                            os.system("rm addons/" + find_addon(user_id, find_open_entry(user_id)["name"])["url"])

                        remove_addon(user_id, find_open_entry(user_id)["name"])
                        # if blend file
                        if using_blender_file:
                            await message.channel.send("<@" + str(message.author.id) + "> Post your blender file next! :cat:")
                        else:
                            await message.channel.send("<@" + str(message.author.id) + "> Updated your old addon! :+1:")

                    else:
                        # if blend file
                        if using_blender_file:
                            await message.channel.send("<@" + str(message.author.id) + "> Post your blender file next! :dog:")
                        else:
                            await message.channel.send("<@" + str(message.author.id) + "> Added your addon to the marketplace! :+1:")

                    # save file
                    await addon_file.save("./addons/" + addon_file.filename.split(".")[0] + str(user_id) + ".py")

                    # put open entry and reference to file in addons.json
                    new_entry = find_open_entry(user_id)
                    new_entry["url"] = addon_file.filename.split(".")[0] + str(user_id) + ".py"
                    add_addon(new_entry)

                    # if not blend file
                    if not using_blender_file:
                        # remove open entry
                        remove_open_entry(user_id)
                        # git push
                        os.system("git add -A")
                        os.system("git commit -m\"Updated or added an addon\"")
                        os.system("git push")

                # if file is .blend
                elif addon_file.filename.split(".")[-1] == "blend":
                    # check if has blender file is true
                    if using_blender_file:
                        # remove open entry
                        remove_open_entry(user_id)
                        # post blender file in the files channel
                        client.get_channel(766772440222138368) # 780780646061703178)
                        channel.send("Hi lol this is a message")
                        #await channel.send(content=addon_file.filename.split(".")[0] + str(user_id) + ".blend", file=addon_file)
                        # post message
                        await message.channel.send("<@" + str(message.author.id) + "> Added your addon to the marketplace! :+1:")
                        # push
                        os.system("git add -A")
                        os.system("git commit -m\"Updated or added an addon\"")
                        os.system("git push")

                else:
                    # "post a proper file"
                    await message.channel.send("<@" + str(message.author.id) + "> Please post a blender or python file!")
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
                        if addon_exists(user_id, find_open_entry(user_id)["name"]):
                            if os.path.exists(os.path.join(os.path.dirname(os.path.realpath(__file__)), "addons", find_addon(user_id, find_open_entry(user_id)["name"])["url"])):
                                os.system("rm addons/" + find_addon(user_id, find_open_entry(user_id)["name"])["url"])

                        remove_addon(user_id, json_message["name"])

                        await message.channel.send("<@" + str(message.author.id) + "> Updated your addon! :+1:")
                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Added your addon to the marketplace! :+1:")

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

            elif message.content.split(" ")[0] == "remove":
                if addon_exists(user_id, message.content[7:]):
                    if os.path.exists(os.path.join(os.path.dirname(os.path.realpath(__file__)), "addons", find_addon(user_id, message.content[7:])["url"])):
                        os.system("rm addons/" + find_addon(user_id, message.content[7:])["url"])

                    remove_addon(user_id, message.content[7:])
                    await message.channel.send("<@" + str(message.author.id) + "> Removed your Addon!")
                    os.system("git add -A")
                    os.system("git commit -m\"Removed an addon\"")
                    os.system("git push")

                else:
                    await message.channel.send("<@" + str(message.author.id) + "> This addon does not exist")

            else:
                # "please try again"
                await message.channel.send("<@" + str(message.author.id) + "> Something went wrong :pensive: Please try again!")

        await message.delete()

client.run(TOKEN)

