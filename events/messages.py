import random
from fuzzywuzzy import fuzz
from ServerMetadata import ServerMetadata
# pass in a message and params to be checked, if params apply, ture is returnd, else false
# TODO: only a single string for now, might want to expand to a list or somethig

s_m = ServerMetadata()


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
    a_emojis = s_m.get_andrew_emojis()
    msg_str = f"<@&{s_m.andew_longo_id}>"
    if await validate_message(msg, prefix='$andrew party'):
        for k in a_emojis:
            await msg.add_reaction(a_emojis[k])
            msg_str += a_emojis[k]
        await msg.channel.send(msg_str)


async def party(msg):
    m = msg.content.lower()

    out_msg = ""
    emojis = {}

    if "everyone" in m:
        out_msg += "@everyone"
        emojis.update(s_m.emojis)

    if "adrian" in m:
        out_msg += f"<@&{s_m.deadlift_daddy_id}>"
        emojis.update(s_m.get_adrian_emojis())
    if "andrew" in m:
        out_msg += f"<@&{s_m.andew_longo_id}>"
        emojis.update(s_m.get_andrew_emojis())
    if "dom" in m:
        out_msg += f"<@&{s_m.pro_brody_lover_id}>"
        emojis.update(s_m.get_dom_emojis())
    if "jessica" in m:
        out_msg += f"<@&{s_m.board_game_master_id}>"
        emojis.update(s_m.get_jessica_emojis())
    if "kito" in m:
        out_msg += f"<@&{s_m.kito_hacker_man_id}>"
        emojis.update(s_m.get_kito_emojis())
    if "lina" in m:
        out_msg += f"<@&{s_m.little_smarty_pants_id}>"
        emojis.update(s_m.get_lina_emojis())
    if "lydia" in m:
        out_msg += f"<@&{s_m.power_dork_id}>"
        emojis.update(s_m.get_lydia_emojis())
    if "mel" in m:
        out_msg += f"<@&{s_m.hamster_mom_id}>"
        emojis.update(s_m.get_mel_emojis())
    if "sally" in m:
        out_msg += f"<@&{s_m.sally_damn_id}>"
        emojis.update(s_m.get_sally_emojis())

    while len(emojis) > 20:
        emojis.pop(random.choice(list(emojis.keys())))

    emojis_l = list(emojis.values())
    random.shuffle(emojis_l)

    for e in emojis_l:
        await msg.add_reaction(e)
        out_msg += e
    await msg.channel.send(out_msg)


async def handle_msg_recv(msg, channel):
    if await validate_message(msg, channel=channel, prefix="$"):
        if "ping" in msg.content:
            await pong(msg)
        elif "party" in msg.content:
            await party(msg)
        else:
            await whos_a_good_boy(msg)
