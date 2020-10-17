import discord
import json
import os

TOKEN = "NzY2NzUyMTU1NzMwMTgyMTg0.X4n7lw.gHoZCW5b7-Er8zF3dlhi10L29J4"
client = discord.Client()
@client.event
async def on_ready():
    print('Connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == 766772440222138368:
        if message.attachments:
            read_file = await message.attachments[0].read()
            file_name = message.attachments[0].filename
            if os.path.exists("./" + file_name):
                with open('./' + file_name, "r+") as new_file:
                    new_file.seek(0)
                    new_file.write(str(read_file))
                    new_file.truncate()
                await message.channel.send("Updated your file :+1:")
            else:
                with open('./' + file_name, "x") as new_file:
                    new_file.seek(0)
                    new_file.write(str(read_file))
                    new_file.truncate()
                await message.channel.send("Added your file :+1:")

            await message.delete()

            with open('./open_entries.json', "r+") as json_file:
                json_file_data = json.load(json_file)
                existing = False
                addon_json = {}
                for x, addon in enumerate(json_file_data["entries"]):
                    if addon["user"] == message.author.id:
                        existing = True
                        addon_json = addon
                        json_file_data["entries"].pop(x)

                json_file.seek(0)
                json_file.write(json.dumps(json_file_data, sort_keys=True, indent=4))
                json_file.truncate()

                if existing:
                    with open('./addons.json', "r+") as json_file:
                        json_file_data = json.load(json_file)
                        addon_json["url"] = "./" + file_name
                        json_file_data["addons"].append(addon_json)
                        json_file.seek(0)
                        json_file.write(json.dumps(json_file_data, sort_keys=True, indent=4))
                        json_file.truncate()

        else:
            try:
                json_data = json.loads(message.content)
            except json.JSONDecodeError:
                json_data = None
        
            await message.delete()

            if json_data:
                json_data["user"] = message.author.id
                if json_data["url"]:
                    with open('./addons.json', "r+") as json_file:
                        json_file_data = json.load(json_file)
                        existing = False
                        for x, addon in enumerate(json_file_data["addons"]):
                            if addon["name"] == json_data["name"] and addon["user"] == json_data["user"]:
                                existing = True
                                json_file_data["addons"][x] = json_data

                        if not existing:
                            json_file_data["addons"].append(json_data)

                        json_file.seek(0)
                        json_file.write(json.dumps(json_file_data, sort_keys=True, indent=4))
                        json_file.truncate()
                    
                        if existing:
                            await message.channel.send("<@" + str(json_data["user"]) + "> Successfully updated your addon! :+1:")
                        else:
                            await message.channel.send("<@" + str(json_data["user"]) + "> Successfully added your addon to the marketplace! :grin:")

                else:
                    with open('./addons.json', "r+") as json_file:
                        json_file_data = json.load(json_file)
                        existing = False
                        for x, addon in enumerate(json_file_data["addons"]):
                            if addon["name"] == json_data["name"] and addon["user"] == json_data["user"]:
                                existing = True
                                json_file_data["addons"][x] = json_data

                        if not existing:
                            with open('./open_entries.json', "r+") as json_file:
                                json_file_data = json.load(json_file)
                                json_file_data["entries"].append(json_data)
                                json_file.seek(0)
                                json_file.write(json.dumps(json_file_data, sort_keys=True, indent=4))
                                json_file.truncate()
                            await message.channel.send("<@" + str(message.author.id) + "> Amazing description! Just post your file next :exploding_head:")

                        else:
                            json_file.seek(0)
                            json_file.write(json.dumps(json_file_data, sort_keys=True, indent=4))
                            json_file.truncate()

                            await message.channel.send("<@" + str(json_data["user"]) + "> Successfully updated your addon! Just post your file now :cat:")
                            
            else:
                await message.channel.send("<@" + str(message.author.id) + "> Something went wrong :pensive:. Please try again or contact an admin")

client.run(TOKEN)

