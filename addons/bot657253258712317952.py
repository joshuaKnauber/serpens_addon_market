# bot.py
import os
import discord
import json
import datetime

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()
@client.event
async def on_ready():
    print('Connected to Discord!')

def generateReadme():
    readme =    ("# **STM32-Discord-Bot Commands**\n\n"
            +   "**List of commands:**\n"
            +   "```")

    with open("./commands.json") as commands:
        commands = json.load(commands)["commands"]
        commands.insert(0, {"command":["help\n"],"result":"List of commands","description":"List of commands","image":None})
        commands.insert(0, {"command":["commands"],"result":"List of moderation commands","description":"List of moderation commands","image":None})

        longestDescription = getLongestDescription(commands)
        longestCommand = getLongestCommand(commands)

        for command in commands:
            line = command["description"]
            line += " " * (longestDescription - len(command["description"]))

            for name in command["command"]:
                line += f"${name}"
                line += " " * (longestCommand - len(name))
            readme += "\n"+line

    readme +=   ("\n```\n"
            +   "**List of moderation commands:**\n"
            +   "```\n"
            +   "add a command                       $commandadd channel(optional) <name> <name> ...\n"
            +   "    type your response or cancel    <response / $>\n"
            +   "    enter a short description       <description>\n"
            +   "    enter an image url or null      <image url / null>\n"
            +   "\n"
            +   "remove a command                    $commandremove <name>\n"
            +   "\n"
            +   "edit a command                      $commandedit <name> name <newname> <newname> ...\n"
            +   "                                    $commandedit <name> response <response>\n"
            +   "                                    $commandedit <name> description <newdescription>\n"
            +   "                                    $commandedit <name> image <imageurl>\n"
            +   "```")

    overwriteReadme(readme)

def overwriteReadme(newReadme):
    with open("./README.md","w") as readme:
        readme.write(newReadme)
        
def getLongestDescription(commands):
    longest = 0
    for command in commands:
        if len(command["description"]) > longest:
            longest = len(command["description"])
    return longest + 2

def getLongestCommand(commands):
    longest = 0
    for command in commands:
        for name in command["command"]:
            if len(name)+1 > longest:
                longest = len(name)+1
    return longest + 2

def hasValidRole(roles, validRoles):
    for role in roles:
        if role.name in validRoles:
            return True
    return False

async def sendText(message, text):
    await message.channel.send(text)

async def sendImage(message, image):
    await message.channel.send(image)

async def executeCommand(message, data, command):
    for command_object in data["commands"]:
        for command_name in command_object["command"]:
            if command_name == command:
                if command_object["channel"]:
                    if command_object["channel"] == message.channel.id:
                        await sendText(message, command_object["result"])
                        if command_object["image"]:
                            await sendImage(message, command_object["image"])
                else:
                    await sendText(message, command_object["result"])
                    if command_object["image"]:
                        await sendImage(message, command_object["image"])

def userIsEditing(author,data):
    if getOldEntry(author, data):
        return True
    return False

def userHasEntryWithResult(author, data):
    if getOldEntry(author, data)["result"] == None:
        return False
    else:
        return True

def userHasEntryWithDescription(author, data):
    if getOldEntry(author, data)["description"] == None:
        return False
    else:
        return True

def getOldEntry(author,data):
    for edit in data["lastadds"]:
        if author == edit["user"]:
            return edit
    return None

def writeJson(data):
    with open("./commands.json", "w") as commands:
        jsonString = json.dumps(data, indent=4)
        commands.write(jsonString)
    generateReadme()

def addJson(key, jsonObject, data):
    data[key].append(jsonObject)
    writeJson(data)

def editJson(key, data, oldEntry, entryKey, value):
    for entry in data[key]:
        if entry == oldEntry:
            entry[entryKey] = value 
    writeJson(data)

def removeJson(key, jsonObject, data):
    data[key].remove(jsonObject)
    writeJson(data)

async def addResult(data, message):
    editJson("lastadds", data, getOldEntry(message.author.name, data), "result", message.content)
    await sendText(message, 'Enter a short description for this command')

async def addDescription(data, message):
    editJson("lastadds", data, getOldEntry(message.author.name, data), "description", message.content)
    await sendText(message, 'Enter an imgur link, or type "null"')

async def finishAdding(data, message):
    jsonObject = getOldEntry(message.author.name, data)
    removeJson("lastadds", jsonObject, data)
    del jsonObject["user"]
    if not message.content.lower() == "null":
        await sendText(message, 'Image added and command is ready to be used!')
        jsonObject["image"] = message.content
    else:
        await sendText(message, 'Command is ready to be used!')
        jsonObject["image"] = None
    addJson("commands", jsonObject, data)

def getCommandEntry(command,data):
    for entry in data["commands"]:
        if command in entry["command"]:
            return entry
    return None

async def commandAdd(message, names, data):
    if len(names) != 0 and names[0] != "channel":
        jsonObject = {"channel": 0, "user": message.author.name, "command": names, "result": None, "description": None}
        addJson("lastadds", jsonObject, data)
        await sendText(message, f"Type your response for {'/'.join(names)} next!")

    elif len(names) >= 2 and names[0] == "channel":
        jsonObject = {"channel": message.channel.id, "user": message.author.name, "command": names[1:], "result": None, "description": None}
        addJson("lastadds", jsonObject, data)
        await sendText(message, f"Type your response for {'/'.join(names[1:])} next!")

    else:
        await sendText(message, "No names found, please try again or type $help")

async def commandRemove(message, commandName, data):
    if len(commandName) != 0:
        entry = getCommandEntry(commandName[0], data)
        if entry:
            removeJson("commands", entry, data)
            await sendText(message, f"Removed {commandName[0]}!")
        else:
            await sendText(message, f"Command '{commandName[0]}' was not found!")
    else:
        await sendText(message, "Please type a command name or $help")

async def commandEdit(message, command, data):
    if len(command) >= 3:
        entry = getCommandEntry(command[0], data)
        if entry == None:
            await sendText(message, f"Command '{command[0]}' not found")
        elif command[1] == "name":
            editJson("commands", data, entry, "command", command[2:])
            await sendText(message, f"Succesfully changed command to '{'/'.join(command[2:])}'")
        elif command[1] == "response":
            editJson("commands", data, entry, "result", ' '.join(command[2:]))
            await sendText(message, f"Succesfully changed the response to '{' '.join(command[2:])}'")
        elif command[1] == "description":
            editJson("commands", data, entry, "description", ' '.join(command[2:]))
            await sendText(message, f"Succesfully changed the description to '{' '.join(command[2:])}'")
        elif command[1] == "image":
            if command[2].lower() == "null":
                editJson("commands", data, entry, "image", None)
            else:
                editJson("commands", data, entry, "image", command[2])
            await sendText(message, f"Succesfully changed the image url to '{command[2]}'")
        else:
            await sendText(message, "Please specify what parameter you want to edit or type $help")
    else:
        await sendText(message, "Please enter all required parameters or type $help")

def get_launchlist_message():
    message = "**Upcoming launches:**\n\n"
    if os.path.exists("launches.json"):
        with open("launches.json") as launchData:
            now = datetime.datetime.utcnow()

            launchData = json.loads(launchData.read())
            if len(launchData) > 5:
                launchData = launchData[:5]

            for launch in launchData:
                launchTime = datetime.datetime(day=launch["time"]["day"],month=launch["time"]["month"],year=launch["time"]["year"],hour=launch["time"]["hour"],minute=launch["time"]["minute"],second=launch["time"]["second"])
                time = launchTime - now
                time = time.total_seconds()
                if time > 0:
                    day = time // 86400
                    day = int(day)
                    time = time - day*86400
                    hour = time // 3600
                    hour = int(hour)
                    time = time - hour*3600
                    minutes = time // 60
                    minutes = int(minutes)
                    
                    message += "• **" + launch["name"] + "** on " + launch["time_raw"] + " or T- "
                    if day:
                        if day == 1:
                            message+=str(day) + " Day"
                        else:
                            message+=str(day) + " Days"
                    if hour:
                        if day:
                            message+=", "
                        if hour == 1:
                            message+=str(hour) + " Hour"
                        else:
                            message+=str(hour) + " Hours"

                    if minutes:
                        if hour or day:
                            message+=", "
                        if minutes == 1:
                            message+=str(minutes) + " Minute"
                        else:
                            message+=str(minutes) + " Minutes"
                    message+="\n"

            if not len(launchData):
                message += "*No upcoming launches found*"
                
    else:
        message += "*No upcoming launches found*"

    return message


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if len(message.content) > 0:

        with open("./commands.json") as commands:
            data = json.load(commands)

        if message.content[0] == "$":
            
            if userIsEditing(message.author.name, data):
                jsonObject = getOldEntry(message.author.name, data)
                removeJson("lastadds", jsonObject, data)

            command = message.content[1:]
            commandSplit = command.split(" ")

            if command == "help":
                with open("./README.md") as helpMessage:
                    await sendText(message, helpMessage.read().split("**List of moderation commands:**")[0])
            if command == "commands":
                with open("./README.md") as helpMessage:
                    msg = "**List of moderation commands:**\n" + helpMessage.read().split("**List of moderation commands:**")[1]
                    await sendText(message, msg)

            else:
                if commandSplit[0] == "launches":
                    await sendText(message, get_launchlist_message())
                elif commandSplit[0] == "commandadd":
                    if hasValidRole(message.author.roles, data["roles"]):
                        await commandAdd(message, commandSplit[1:], data)
                    else:
                        await sendText(message, "You do not have permission to use this command!")
                elif commandSplit[0] == "commandedit":
                    if hasValidRole(message.author.roles, data["roles"]):
                        await commandEdit(message, commandSplit[1:], data)
                    else:
                        await sendText(message, "You do not have permission to use this command!")
                elif commandSplit[0] == "commandremove":
                    if hasValidRole(message.author.roles, data["roles"]):
                        await commandRemove(message, commandSplit[1:], data)
                    else:
                        await sendText(message, "You do not have permission to use this command!")
                else:
                    await executeCommand(message, data, command)

        elif userIsEditing(message.author.name, data):
            if not userHasEntryWithResult(message.author.name, data):
                await addResult(data, message)
            elif not userHasEntryWithDescription(message.author.name, data):
                await addDescription(data, message)
            else:
                await finishAdding(data, message)


client.run(TOKEN)