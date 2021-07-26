import discord
import pathlib
import random
import json
import os
from discord import user
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

def add_snippet(snippet_json):
    with open("./snippets.json", "r+") as snippets:
        snippets_json = json.load(snippets)
        snippets_json["snippets"].append(snippet_json)
        snippets.seek(0)
        snippets.write(json.dumps(snippets_json, skipkeys=True, indent=4))
        snippets.truncate()


def add_package(package_json):
    with open("./packages.json", "r+") as packages:
        packages_json = json.load(packages)
        packages_json["packages"].append(package_json)
        packages.seek(0)
        packages.write(json.dumps(packages_json, skipkeys=True, indent=4))
        packages.truncate()


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
                open_entries[user_id] = {"type": "addon", "json": {}}
                await message.channel.send("<@" + str(message.author.id) + "> You want to upload an Addon! Cool! Just send me the message you got in serpens and paste it in here! You can type **Cancel** at any time to stop your upload process!")
            elif message.content.lower() in ["snippet", "s"]:
                open_entries[user_id] = {"type": "snippet", "json": {"title": "","description": "","price": "","url": "", "blend_url": "", "author": ""}}
                await message.channel.send("<@" + str(message.author.id) + "> You want to upload a Snippet! Awesome! You can type **Cancel** at any time to stop your upload process! Now let me know what do you want to call it!")
            elif message.content.lower() in ["package", "p"]:
                open_entries[user_id] = {"type": "package", "json": {"title": "","description": "","price": "","url": "","author": ""}}
                await message.channel.send("<@" + str(message.author.id) + "> You want to upload a Package! Great! You can type **Cancel** at any time to stop your upload process! Now let me know what do you want to call it!")
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
                        open_entries[user_id]["json"]["user"] = user_id
                        if open_entries[user_id]["json"]["external"]:
                            if open_entries[user_id]["json"]["blend"]:
                                await message.channel.send("<@" + str(message.author.id) + "> Send me your blend file next!")
                            else:
                                add_addon(open_entries[user_id]["json"])
                                open_entries.pop(user_id)
                                await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your addon!")
                        else:
                            await message.channel.send("<@" + str(message.author.id) + "> Send me your addons zip file next!")
                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Please send me the message you copied in serpens first or type **Cancel**!")
                else:
                    if message.attachments:
                        addon_file = message.attachments[0]
                        file_name = addon_file.filename
                        if not open_entries[user_id]["json"]["external"] and not open_entries[user_id]["json"]["url"]:
                            if ".zip" in file_name:
                                open_entries[user_id]["json"]["url"] = await save_file(addon_file)
                                if open_entries[user_id]["json"]["blend"]:
                                    await message.channel.send("<@" + str(message.author.id) + "> Send me your blend file next!")
                                else:
                                    add_addon(open_entries[user_id]["json"])
                                    open_entries.pop(user_id)
                                    await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your addon!")
                            else:
                                await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")

                        elif open_entries[user_id]["json"]["blend"]:
                            if ".blend" in file_name:
                                open_entries[user_id]["json"]["blend_url"] = await save_file(addon_file)
                                add_addon(open_entries[user_id]["json"])
                                open_entries.pop(user_id)
                                await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your addon and blend file!")
                            else:
                                await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")
                        else:
                            await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")

                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")

            elif open_entries[user_id]["type"] == "snippet":
                if not open_entries[user_id]["json"]["title"]:
                    open_entries[user_id]["json"]["title"] = message.content
                    await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> Got it! Now send me a description!")

                elif not open_entries[user_id]["json"]["description"]:
                    open_entries[user_id]["json"]["description"] = message.content
                    await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> Alright! I need an author next!")

                elif not open_entries[user_id]["json"]["author"]:
                    open_entries[user_id]["json"]["author"] = message.content
                    await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> Nice! Now I need a price or just type **Free**!")

                elif not open_entries[user_id]["json"]["price"]:
                    open_entries[user_id]["json"]["price"] = message.content
                    await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> Type **Yes** if you want to upload a file directly and **No** if you have an external url!")

                elif not open_entries[user_id]["json"]["url"]:
                    if message.content.lower() == "yes":
                        open_entries[user_id]["json"]["url"] = "yes"
                        await message.channel.send("<@" + str(message.author.id) + "> You want to upload a file directly! Just send it in here and I will upload it!")
                    elif message.content.lower() == "no":
                        open_entries[user_id]["json"]["url"] = "no"
                        await message.channel.send("<@" + str(message.author.id) + "> So you have an external url! Paste it in here and I will upload it")
                    else:
                        await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> I didn't get that. Please type **Yes**, **No** or **Cancel**!")
                
                elif open_entries[user_id]["json"]["url"] == "yes":
                    if message.attachments:
                        addon_file = message.attachments[0]
                        file_name = addon_file.filename
                        if ".zip" in file_name or ".json" in file_name:
                            open_entries[user_id]["json"]["url"] = await save_file(addon_file)
                            await message.channel.send("<@" + str(message.author.id) + "> Last question! Type **Yes** if you want to upload a blend file and **No** if you don't")
                        else:
                            await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")

                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")

                elif open_entries[user_id]["json"]["url"] == "no":
                    open_entries[user_id]["json"]["url"] = message.content
                    await message.channel.send("<@" + str(message.author.id) + "> Last question! Type **Yes** if you want to upload a blend file and **No** if you don't")

                elif not open_entries[user_id]["json"]["blend_url"]:
                    if message.content.lower() == "yes":
                        open_entries[user_id]["json"]["blend_url"] = "yes"
                        await message.channel.send("<@" + str(message.author.id) + "> You want to upload a blend file! Just send it in here and I will upload it!")
                    elif message.content.lower() == "no":
                        add_snippet(open_entries[user_id]["json"])
                        open_entries.pop(user_id)
                        await message.channel.send("<@" + str(message.author.id) + "> You're done! Thanks for uploading your snippet!")
                    else:
                        await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> I didn't get that. Please type **Yes**, **No** or **Cancel**!")

                elif open_entries[user_id]["json"]["blend_url"] == "yes":
                    if message.attachments:
                        blend_file = message.attachments[0]
                        file_name = blend_file.filename
                        if ".blend" in file_name:
                            open_entries[user_id]["json"]["blend_url"] = await save_file(blend_file)
                            add_snippet(open_entries[user_id]["json"])
                            open_entries.pop(user_id)
                            await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your snippet and blend file!")
                        else:
                            await message.channel.send("<@" + str(message.author.id) + "> Please upload a blend file or type **Cancel**!")
                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")

            elif open_entries[user_id]["type"] == "package":
                if not open_entries[user_id]["json"]["title"]:
                    open_entries[user_id]["json"]["title"] = message.content
                    await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> Got it! Now send me a description!")

                elif not open_entries[user_id]["json"]["description"]:
                    open_entries[user_id]["json"]["description"] = message.content
                    await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> Alright! I need an author next!")

                elif not open_entries[user_id]["json"]["author"]:
                    open_entries[user_id]["json"]["author"] = message.content
                    await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> Nice! Now I need a price or just type **Free**!")

                elif not open_entries[user_id]["json"]["price"]:
                    open_entries[user_id]["json"]["price"] = message.content
                    await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> Now send me the link to the download page!")

                elif not open_entries[user_id]["json"]["url"]:
                    open_entries[user_id]["json"]["url"] = message.content
                    add_package(open_entries[user_id]["json"])
                    open_entries.pop(user_id)
                    await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your package!")


        await message.delete()
        os.system("git add -A")
        os.system("git commit -m\"Serverlog\"")
        os.system("git pull")
        os.system("git push")


client.run(TOKEN)

