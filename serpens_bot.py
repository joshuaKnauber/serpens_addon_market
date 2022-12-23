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

def find_addons(user_id):
    addon_list = []
    with open("./addons.json") as addons:
        addons = json.load(addons)
        for entry in addons["addons"]:
            if entry["user"] == user_id:
                addon_list.append(entry)
    return addon_list

def find_snippets(user_id):
    snippet_list = []
    with open("./snippets.json") as snippets:
        snippets = json.load(snippets)
        for entry in snippets["snippets"]:
            if entry["user"] == user_id:
                snippet_list.append(entry)
    return snippet_list

def find_packages(user_id):
    packages_list = []
    with open("./packages.json") as packages:
        packages = json.load(packages)
        for entry in packages["packages"]:
            if entry["user"] == user_id:
                packages_list.append(entry)
    return packages_list

def get_addon(user_id, name):
    addon = {}
    for entry in find_addons(user_id):
        if entry["name"] == name:
            addon = entry
    return addon

def get_snippet(user_id, title):
    snippet = {}
    for entry in find_snippets(user_id):
        if entry["title"] == title:
            snippet = entry
    return snippet

def get_package(user_id, title):
    package = {}
    for package_entry in find_packages(user_id):
        if package_entry["title"] == title:
            package = package_entry
    return package

def remove_addon(user_id, name):
    with open("./addons.json", "r+") as addons:
        addons_json = json.load(addons)
        for x, entry in enumerate(addons_json["addons"]):
            if entry["user"] == user_id and entry["name"] == name:
                addons_json["addons"].pop(x)
        addons.seek(0)
        addons.write(json.dumps(addons_json, skipkeys=True, indent=4))
        addons.truncate()

def remove_snippet(user_id, name):
    with open("./snippets.json", "r+") as snippets:
        snippet_json = json.load(snippets)
        for x, entry in enumerate(snippet_json["snippets"]):
            if entry["user"] == user_id and entry["title"] == name:
                snippet_json["snippets"].pop(x)
        snippets.seek(0)
        snippets.write(json.dumps(snippet_json, skipkeys=True, indent=4))
        snippets.truncate()

def remove_package(user_id, name):
    with open("./packages.json", "r+") as packages:
        packages_json = json.load(packages)
        for x, entry in enumerate(packages_json["packages"]):
            if entry["user"] == user_id and entry["title"] == name:
                packages_json["packages"].pop(x)
        packages.seek(0)
        packages.write(json.dumps(packages_json, skipkeys=True, indent=4))
        packages.truncate()

def add_addon(addon_json):
    with open("./addons.json", "r+") as addons:
        addons_json = json.load(addons)
        addons_json["addons"].append(addon_json)
        addons.seek(0)
        addons.write(json.dumps(addons_json, skipkeys=True, indent=4))
        addons.truncate()


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

    os.system("rm -rf" + file_name)

    return message.attachments[0].url

async def save_snippet(save_file, user_id):
    file_name = save_file.filename
    channel = client.get_channel(785132940278366260)

    await save_file.save(file_name)
    if file_name.split(".")[-1] == "zip":
        with open(file_name,"r+") as file_text:
            snippet = json.loads(file_text.read())
            if "version" in snippet:
                open_entries[user_id]["json"]["serpens_version"] = snippet["version"]
    fileobject = discord.File(file_name)
    message = await channel.send(file=fileobject)

    os.system("rm -rf" + file_name)

    return message.attachments[0].url

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if message in addon-market or commands
    if message.channel.id in [767853772562366514, 768053288989360128]:
        user_id = message.author.id

        if not user_id in open_entries:
            if message.content.lower() in ["update", "upload", "remove"]:
                open_entries[user_id] = {"upload_type": message.content.lower(), "type": ""}
                await message.channel.send("<@" + str(message.author.id) + "> You want to " + message.content.lower() + " something! Cool! Just type:\n\n- **Addon** or **A** for addon\n- **Snippet** or **S** for snippet\n- **Package** or **P** for package")
            else:
                await message.channel.send("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n<@" + str(message.author.id) + ">" + random_emoji() + " Hey, I don't have a conversation with you yet, just type:\n\n- **Upload** for uploading\n- **Update** for updating\n- **Remove** for removing")


        elif message.content.lower() == "cancel":
            open_entries.pop(user_id)
            await message.channel.send("<@" + str(message.author.id) + "> I canceled your upload! Feel free to try again at any time!")


        elif open_entries[user_id]["type"] == "":
            if message.content.lower() in ["addon", "a"]:
                open_entries[user_id]["type"] = "addon"
                open_entries[user_id]["json"] =  {}
                if open_entries[user_id]["upload_type"] == "upload":
                    await message.channel.send("<@" + str(message.author.id) + "> You want to " + open_entries[user_id]["upload_type"] + " an Addon! Cool! Just send me the message you got in serpens and paste it in here! You can type **Cancel** at any time!")
                elif open_entries[user_id]["upload_type"] == "remove":
                    addon_string = ""
                    for addon in find_addons(user_id):
                        addon_string += "- " + addon["name"] + "\n"
                    if addon_string:
                        await message.channel.send("<@" + str(message.author.id) + "> I found the following addons:\n" + addon_string + "Just type out the one you want to remove!")
                    else:
                        open_entries.pop(user_id)
                        await message.channel.send("<@" + str(message.author.id) + "> Seems like you don't have an addon uploaded")
                elif open_entries[user_id]["upload_type"] == "update":
                    open_entries[user_id]["name"] = ""
                    addon_string = ""
                    for addon in find_addons(user_id):
                        addon_string += "- " + addon["name"] + "\n"
                    if addon_string:
                        await message.channel.send("<@" + str(message.author.id) + "> I found the following addons:\n" + addon_string + "Just type out the one you want to update!")
                    else:
                        open_entries.pop(user_id)
                        await message.channel.send("<@" + str(message.author.id) + "> Seems like you don't have an addon uploaded")

            elif message.content.lower() in ["snippet", "s"]:
                open_entries[user_id]["type"] = "snippet"
                open_entries[user_id]["json"] =  {"title": "","description": "","price": "","url": "", "blend_url": "", "author": "", "user": user_id}
                if open_entries[user_id]["upload_type"] == "upload":
                    await message.channel.send("<@" + str(message.author.id) + "> You want to " + open_entries[user_id]["upload_type"] + " a Snippet! Awesome! You can type **Cancel** at any time! Now let me know what do you want to call it!")
                elif open_entries[user_id]["upload_type"] == "remove":
                    snippet_string = ""
                    for snippet in find_snippets(user_id):
                        snippet_string += "- " + snippet["title"] + "\n"
                    if snippet_string:
                        await message.channel.send("<@" + str(message.author.id) + "> I found the following snippets:\n" + snippet_string + "Just type out the one you want to remove!")
                    else:
                        open_entries.pop(user_id)
                        await message.channel.send("<@" + str(message.author.id) + "> Seems like you don't have a snippet uploaded")
                elif open_entries[user_id]["upload_type"] == "update":
                    snippet_string = ""
                    for snippet in find_snippets(user_id):
                        snippet_string += "- " + snippet["title"] + "\n"
                    if snippet_string:
                        await message.channel.send("<@" + str(message.author.id) + "> I found the following snippets:\n" + snippet_string + "Just type out the one you want to update!")
                    else:
                        open_entries.pop(user_id)
                        await message.channel.send("<@" + str(message.author.id) + "> Seems like you don't have a snippet uploaded")

            elif message.content.lower() in ["package", "p"]:
                open_entries[user_id]["type"] = "package"
                open_entries[user_id]["json"] =  {"title": "","description": "","price": "","url": "", "author": "", "user": user_id}
                if open_entries[user_id]["upload_type"] == "upload":
                    await message.channel.send("<@" + str(message.author.id) + "> You want to " + open_entries[user_id]["upload_type"] + " a Package! Great! You can type **Cancel** at any time! Now let me know what do you want to call it!")
                elif open_entries[user_id]["upload_type"] == "remove":
                    packages_string = ""
                    for package in find_packages(user_id):
                        packages_string += "- " + package["title"] + "\n"
                    if packages_string:
                        await message.channel.send("<@" + str(message.author.id) + "> I found the following packages:\n" + packages_string + "Just type out the one you want to remove!")
                    else:
                        open_entries.pop(user_id)
                        await message.channel.send("<@" + str(message.author.id) + "> Seems like you don't have a package uploaded")
                elif open_entries[user_id]["upload_type"] == "update":
                    packages_string = ""
                    for package in find_packages(user_id):
                        packages_string += "- " + package["title"] + "\n"
                    if packages_string:
                        await message.channel.send("<@" + str(message.author.id) + "> I found the following packages:\n" + packages_string + "Just type out the one you want to update!")
                    else:
                        open_entries.pop(user_id)
                        await message.channel.send("<@" + str(message.author.id) + "> Seems like you don't have a package uploaded")

            else:
                await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")


        elif open_entries[user_id]["upload_type"] == "update":
            if open_entries[user_id]["type"] == "addon":
                if not open_entries[user_id]["name"]:
                    addon_names = {}
                    for addon in find_addons(user_id):
                        addon_names[addon["name"].lower()] = addon["name"]
                    if message.content.lower() in addon_names:
                        open_entries[user_id]["name"] = addon_names[message.content.lower()]
                        await message.channel.send("<@" + str(message.author.id) + "> Got it! Next send me the new message you copied in serpens!")
                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")
                elif not open_entries[user_id]["json"]:
                    if is_valid_json(message.content):
                        open_entries[user_id]["json"] = json.loads(message.content)
                        open_entries[user_id]["json"]["user"] = user_id
                        if open_entries[user_id]["json"]["external"]:
                            if open_entries[user_id]["json"]["blend"]:
                                await message.channel.send("<@" + str(message.author.id) + "> Send me your blend file next!")
                            else:
                                remove_addon(user_id, open_entries[user_id]["name"])
                                add_addon(open_entries[user_id]["json"])
                                open_entries.pop(user_id)
                                await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your addon! It might take a few minutes to show up on the marketplace!")
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
                                    remove_addon(user_id, open_entries[user_id]["name"])
                                    add_addon(open_entries[user_id]["json"])
                                    open_entries.pop(user_id)
                                    await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your addon!")
                            else:
                                await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")

                        elif open_entries[user_id]["json"]["blend"]:
                            if ".blend" in file_name:
                                open_entries[user_id]["json"]["blend_url"] = await save_file(addon_file)
                                remove_addon(user_id, open_entries[user_id]["name"])
                                add_addon(open_entries[user_id]["json"])
                                open_entries.pop(user_id)
                                await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your addon and blend file! It might take a few minutes to show up on the marketplace!")
                            else:
                                await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")
                        else:
                            await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")

                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")

            elif open_entries[user_id]["type"] == "snippet":
                if not open_entries[user_id]["json"]["title"]:
                    snippet_names = {}
                    for snippet in find_snippets(user_id):
                        snippet_names[snippet["title"].lower()] = snippet["title"]
                    if message.content.lower() in snippet_names:
                        open_entries[user_id]["json"]["title"] = snippet_names[message.content.lower()]
                        await message.channel.send("<@" + str(message.author.id) + "> Got it! Your current description is:\n'" + get_snippet(user_id, snippet_names[message.content.lower()])["description"] + "'\nType a new description or just copy and paste this one again!")
                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")

                elif not open_entries[user_id]["json"]["description"]:
                    open_entries[user_id]["json"]["description"] = message.content
                    await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> Alright! Your current author is:\n'" + get_snippet(user_id, open_entries[user_id]["json"]["title"])["author"] + "'\nType a new author or just copy and paste this one again!")
                
                elif not open_entries[user_id]["json"]["author"]:
                    open_entries[user_id]["json"]["author"] = message.content
                    await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> Cool! Your current price is:\n'" + get_snippet(user_id, open_entries[user_id]["json"]["title"])["price"] + "'\nType a new price or just copy and paste this one again!")
                
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
                            open_entries[user_id]["json"]["url"] = await save_snippet(addon_file, user_id)
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
                        remove_snippet(user_id, open_entries[user_id]["json"]["title"])
                        add_snippet(open_entries[user_id]["json"])
                        open_entries.pop(user_id)
                        await message.channel.send("<@" + str(message.author.id) + "> You're done! Thanks for updating your snippet! It might take a few minutes to change on the marketplace!")
                    else:
                        await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> I didn't get that. Please type **Yes**, **No** or **Cancel**!")

                elif open_entries[user_id]["json"]["blend_url"] == "yes":
                    if message.attachments:
                        blend_file = message.attachments[0]
                        file_name = blend_file.filename
                        if ".blend" in file_name:
                            open_entries[user_id]["json"]["blend_url"] = await save_file(blend_file)
                            remove_snippet(user_id, open_entries[user_id]["json"]["title"])
                            add_snippet(open_entries[user_id]["json"])
                            open_entries.pop(user_id)
                            await message.channel.send("<@" + str(message.author.id) + "> Thanks for updating your snippet and blend file! It might take a few minutes to change on the marketplace!")
                        else:
                            await message.channel.send("<@" + str(message.author.id) + "> Please upload a blend file or type **Cancel**!")
                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")


            elif open_entries[user_id]["type"] == "package":
                if not open_entries[user_id]["json"]["title"]:
                    package_names = {}
                    for package in find_packages(user_id):
                        package_names[package["title"].lower()] = package["title"]
                    if message.content.lower() in package_names:
                        open_entries[user_id]["json"]["title"] = package_names[message.content.lower()]
                        await message.channel.send("<@" + str(message.author.id) + "> Got it! Your current description is:\n'" + get_package(user_id, package_names[message.content.lower()])["description"] + "'\nType a new description or just copy and paste this one again!")
                    else:
                        await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")

                elif not open_entries[user_id]["json"]["description"]:
                    open_entries[user_id]["json"]["description"] = message.content
                    await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> Alright! Your current author is:\n'" + get_package(user_id, open_entries[user_id]["json"]["title"])["author"] + "'\nType a new author or just copy and paste this one again!")
                
                elif not open_entries[user_id]["json"]["author"]:
                    open_entries[user_id]["json"]["author"] = message.content
                    await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> Cool! Your current price is:\n'" + get_package(user_id, open_entries[user_id]["json"]["title"])["price"] + "'\nType a new price or just copy and paste this one again!")
                
                elif not open_entries[user_id]["json"]["price"]:
                    open_entries[user_id]["json"]["price"] = message.content
                    await message.channel.send("- " + message.content + "\n\n<@" + str(message.author.id) + "> Your current url is:\n'" + get_package(user_id, open_entries[user_id]["json"]["title"])["url"] + "'\nType a new url or just copy and paste this one again!")

                elif not open_entries[user_id]["json"]["url"]:
                    open_entries[user_id]["json"]["url"] = message.content
                    remove_package(user_id, open_entries[user_id]["json"]["title"])
                    add_package(open_entries[user_id]["json"])
                    open_entries.pop(user_id)
                    await message.channel.send("<@" + str(message.author.id) + "> Thanks for updating your package! It might take a few minutes to change on the marketplace!")


        elif open_entries[user_id]["upload_type"] == "remove":
            if open_entries[user_id]["type"] == "addon":
                addon_names = {}
                for addon in find_addons(user_id):
                    addon_names[addon["name"].lower()] = addon["name"]
                if message.content.lower() in addon_names:
                    remove_addon(user_id, addon_names[message.content.lower()])
                    open_entries.pop(user_id)
                    await message.channel.send("<@" + str(message.author.id) + "> Removed your addon! It might take a few minutes to get removed from the marketplace!")
                else:
                    await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")

            elif open_entries[user_id]["type"] == "snippet":
                snippet_names = {}
                for snippet in find_snippets(user_id):
                    snippet_names[snippet["title"].lower()] = snippet["title"]
                if message.content.lower() in snippet_names:
                    remove_snippet(user_id, snippet_names[message.content.lower()])
                    open_entries.pop(user_id)
                    await message.channel.send("<@" + str(message.author.id) + "> Removed your snippet! It might take a few minutes to get removed from the marketplace!")
                else:
                    await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")

            elif open_entries[user_id]["type"] == "package":
                package_names = {}
                for package in find_packages(user_id):
                    package_names[package["title"].lower()] = package["title"]
                if message.content.lower() in package_names:
                    remove_package(user_id, package_names[message.content.lower()])
                    open_entries.pop(user_id)
                    await message.channel.send("<@" + str(message.author.id) + "> Removed your package! It might take a few minutes to get removed from the marketplace!")
                else:
                    await message.channel.send("<@" + str(message.author.id) + "> Something went wrong there. Please try again or type **Cancel**!")


        elif open_entries[user_id]["upload_type"] == "upload":
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
                                await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your addon! It might take a few minutes to show up on the marketplace!")
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
                                await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your addon and blend file! It might take a few minutes to show up on the marketplace!")
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
                            open_entries[user_id]["json"]["url"] = await save_snippet(addon_file, user_id)
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
                        await message.channel.send("<@" + str(message.author.id) + "> You're done! Thanks for uploading your snippet! It might take a few minutes to show up on the marketplace!")
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
                            await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your snippet and blend file! It might take a few minutes to show up on the marketplace!")
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
                    open_entries[user_id]["json"]["version"] = 3
                    add_package(open_entries[user_id]["json"])
                    open_entries.pop(user_id)
                    await message.channel.send("<@" + str(message.author.id) + "> Thanks for uploading your package! It might take a few minutes to show up on the marketplace!")


        await message.delete()
        os.system("git add -A")
        os.system("git commit -m\"Serverlog\"")
        os.system("git pull")
        os.system("git push")


client.run(TOKEN)

