import discord
import asyncio
from executeStmt import execStmt
from executeStmt import getHelloWorld
from executeStmt import getLanguages

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    content = message.content.split(None, 2)
    print(message.channel.id)
    if message.channel.id == "42936799903221410" or message.channel.id == "42061486042480640":
        if len(content) == 3 and content[0] == "!code": #Check if there is code being run
            try:
                lang = content[1]
                if content[0] == "!code" and content[2] == "HelloWorld": #Handle hello world requests
                    await client.send_message(message.channel, getHelloWorld(lang))
                else:
                    if(content[2].count("```") == 2):
                        code = content[2][3:len(content[2]) - 3]
                    else:
                        code = content[2]
                    output = execStmt(lang, code)
                    await client.send_message(message.channel, output)
            except Exception as e:
                await client.send_message(message.channel, repr(e))
        elif content[0] == "!code" and content[1] == "help":
            help = "Type `!code language ```code``` ` to run code! Ex. `!code python ```print(42)``` ` To get an example hello world script for a language, type `!code language HelloWorld`. Type `!code languages` to see a list of available languages."
            await client.send_message(message.channel, help)
        elif content[0] == "!code" and content[1] == "languages":
            langList = getLanguages()
            print(langList)
            msg = "List of languages:\n```\n"
            for lang in langList:
                print(lang)
                msg += lang + "\n"
            msg += "```"
            await client.send_message(message.channel, msg)
    if message.channel.id == "30283938796337152" and message.content.startswith(";cs"):
        await client.send_message(client.get_channel("42936799032721410"), message.content[4:])

client.run('')
