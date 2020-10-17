import discord
import json
import os

TOKEN = ""
client = discord.Client()
@client.event
async def on_ready():
    print('Connected to Discord!')


def has_open_entry(user_id):
    with open("./open_entries.json") as open_entries:
        open_entries = json.loads(open_entries)
        for entry in open_entries["entries"]:
            if entry["user"] == user_id:
                return True
    return False

def find_open_entry(user_id):
    with open("./open_entries.json") as open_entries:
        open_entries = json.loads(open_entries)
        for entry in open_entries["entries"]:
            if entry["user"] == user_id:
                return entry
    return None

def remove_open_entry(user_id):
    with open("./open_entries.json") as open_entries:
        open_entries_json = json.loads(open_entries)
        for x, entry in open_entries_json["addons"]:
            if entry["user"] == user_id:
                open_entries_json.pop(x)
        open_entries.seek(0)
        open_entries.write(json.dumps(open_entries_json, skipkeys=True, indent=4))
        open_entries.close()

def add_open_entry(entry_json):
    with open("./open_entries.json") as open_entries:
        open_entries_json = json.loads(open_entries)
        open_entries_json.append(entry_json)
        open_entries.seek(0)
        open_entries.write(json.dumps(open_entries_json, skipkeys=True, indent=4))
        open_entries.close()

def addon_exists(user_id, name):
    with open("./addons.json") as addons:
        addons = json.loads(addons)
        for entry in addons["addons"]:
            if entry["user"] == user_id and entry["name"] == name:
                return True
    return False

def remove_addon(user_id, name):
    with open("./addons.json", "r+") as addons:
        addons_json = json.loads(addons)
        for x, entry in addons_json["addons"]:
            if entry["user"] == user_id and entry["name"] == name:
                addons_json.pop(x)
        addons.seek(0)
        addons.write(json.dumps(addons_json, skipkeys=True, indent=4))
        addons.close()

def add_addon(addon_json):
    with open("./addons.json", "r+") as addons:
        addons_json = json.loads(addons)
        addons_json.append(addon_json)
        addons.seek(0)
        addons.write(json.dumps(addons_json, skipkeys=True, indent=4))
        addons.close()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == 7667724402221383680:
        # if message is a file
        if message.attachments:
            addon_file = message.attachments[0]
            user_id = message.author.id
            # if user has open entry
            if has_open_entry(user_id):
                # if file is python file
                if addon_file.file_name.split(".")[-1] == "py":
                    #TODO set filename
                    # save file
                    await addon_file.save("something.py")
                    # if exists in addons.json
                    if addon_exists(user_id, find_open_entry(user_id)["name"]):
                        # delete old data
                        remove_addon(user_id, name)

                    # put open entry and reference to file in addons.json
                    new_entry = find_open_entry(user_id)
                    new_entry["url"] = "./something.py"
                    add_addon(new_entry)
                    # remove open entry
                    remove_open_entry(user_id)
                
                else:
                    await
                # else
                    # "post your python file"
            # else
                # "post your message first"

        else:
            pass
            # if is valid json
                # if using url
                    # if exists in addons.json
                        # overwrite old data with new data
                    # else
                        # add new data to file
                # else
                    # if has openentry
                        # delete old entry
                    # add new entry
            # else
                # "please try again"

        await message.delete()
        await message.channel.send("<@" + str(message.author.id) + "> Nice")

client.run(TOKEN)

