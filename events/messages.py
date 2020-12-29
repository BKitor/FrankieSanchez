from fuzzywuzzy import fuzz
from emojis import emojis
# pass in a message and params to be checked, if params apply, ture is returnd, else false
# TODO: only a single string for now, might want to expand to a list or somethig


async def validate_message(msg, channel=None, prefix=None, author=None):
    if channel is not None and msg.channel.name != channel:
        return False

    if author is not None and msg.author.name != author:
        return False

    if prefix is not None and not msg.content.startswith(prefix):
        return False

    return True


async def whos_a_good_boy(msg):
    m = msg.content[1:].lower()
    identifier = "who's a good boy"

    # 85 is a bit arbitrary, might want to change later
    if fuzz.partial_ratio(m, identifier) < 85:
        return

    response = "Woof Woof 🐶"
    if await validate_message(msg, author="domo"):
        response = "Dont' talk to me Domo"

    await msg.channel.send(response)


async def pong(msg):
    delete_after = 2
    await msg.channel.send("pong", delete_after=delete_after)
    await msg.delete(delay=delete_after)


async def andrew_party(msg):
    if await validate_message(msg, prefix='$andrew party'):
        for k in emojis:
            await msg.add_reaction(emojis[k])
        await msg.channel.send("<@&788493761373667430>"+emojis["ANDREW_HAHA"]+emojis["LONGO"]+emojis["ANDREW_CONCENTRATE"]+emojis["ANDREW_FRANCH"]+emojis["ANDREW_SAD"])


async def handle_msg_recv(msg, channel):
    if await validate_message(msg, channel=channel, prefix="$"):
        if "ping" in msg.content:
            await pong(msg)
        else:
            await whos_a_good_boy(msg)
            await andrew_party(msg)
