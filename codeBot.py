import discord
import asyncio
from executeStmt import execStmt
from executeStmt import getHelloWorld
from executeStmt import getLanguages

codeBot_Channel_ID = "Enter ID of channel you want code bot to run in"

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
    if message.channel.id == codeBot_Channel_ID:
        if len(content) == 3 and content[0] == "!code": #Check if there is code being run
            try:
                lang = content[1]
                if content[0] == "!code" and content[2] == "HelloWorld": #Handle hello world request
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
            msg = "List of languages:\n```\n"
            for lang in langList:
                print(lang)
                msg += lang + "\n"
            msg += "```"
            await client.send_message(message.channel, msg)
client.run('Enter_token_here')
