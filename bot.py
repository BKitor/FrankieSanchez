#!/home/bkitor/Projects/FrankieSanchez/venv/bin/python
import os
import discord
from dotenv import load_dotenv
from messages import handle_msg_recv
load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


@client.event
async def on_message_delete(message):
    print("saw that delete")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(r'%'):
        await handle_msg_recv(message)


@client.event
async def on_reaction_add(reaction, user):
    print("saw that reaction")
    await reaction.message.channel.send('saw that')

client.run(os.getenv("DISCORD_BOT_TOKEN"))
