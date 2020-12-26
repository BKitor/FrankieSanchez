#!/home/bkitor/Documents/Projects/FrankieSanchez/venv/bin/python
import os
import discord
from dotenv import load_dotenv
from events.messages import handle_msg_recv
load_dotenv()

main_channel = "the-chitty-chat" if not os.getenv("BOT_DEBUG") else "tst_gnrl"

client = discord.Client()

@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


@client.event
async def on_message_delete(message):
    pass


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f"message from {message.author.name} in {message.channel} contents {message.content}")

    await handle_msg_recv(message, main_channel)


@client.event
async def on_reaction_add(reaction, user):
    pass

client.run(os.getenv("DISCORD_BOT_TOKEN"))
