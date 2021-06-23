"""
Talia Discord Bot
GNU General Public License v3.0
pickaxe.py (Commands/Earning)

pickaxe command
"""
import asyncio
import discord_components
from Utils import user, message, abc, other
from Storage import help_list

#   Command Information   #
name = "pickaxe"
dm_capable = True
# ~~~~~~~~~~~~~~~~~~~~~~~ #

pickaxes = {
    1: {
        "name": "Bronze Pickaxe",
        "cost": 150,
        "speed": 1,
        "multiplier": 1.0
    },
    2: {
        "name": "Steel Pickaxe",
        "cost": 800,
        "speed": 2,
        "multiplier": 1.1
    },
    3: {
        "name": "Laser Pickaxe",
        "cost": 3000,
        "speed": 3,
        "multiplier": 1.3
    },
    4: {
        "name": "Mithril Pickaxe",
        "cost": 10000,
        "speed": 4,
        "multiplier": 1.5
    },
    5: {
        "name": "Infinity Pickaxe",
        "cost": 40000,
        "speed": 5,
        "multiplier": 1.7
    },
    6: {
        "name": "Universal Pickaxe",
        "cost": 100000,
        "speed": 6,
        "multiplier": 2
    }
}


async def run(bot, msg, conn):
    split_data = msg.content.split(" ")

    if len(split_data) < 2:
        await message.invalid_use(msg, help_list.pickaxe, "No operation given")
        return

    split_data[1] = split_data[1].lower()

    if split_data[1] == "buy":
        await _pickaxe_buy(bot, msg, conn, split_data)

    elif split_data[1] == "sell":
        await _pickaxe_sell(bot, msg, conn)

    elif split_data[1] == "list":
        await _pickaxe_list(bot, msg)

    else:
        await message.send_error(msg, f"Unknown operation: {split_data[1]}")


async def _pickaxe_buy(bot, msg, conn, split_data):
    if len(split_data) < 3:
        await message.invalid_use(msg, help_list.pickaxe, "No pickaxe given")
        return

    userinfo = user.load_user(msg.author.id, conn)

    if userinfo.pickaxe is not None:
        await message.send_error(msg, "You already have a pickaxe")
        return

    try:
        pickaxe_id = int(split_data[2])
    except ValueError:
        await message.send_error(msg, "Invalid pickaxe ID")
        return

    if pickaxe_id not in pickaxes:
        await message.send_message(msg, "There's no pickaxe with that ID")
        return

    if pickaxes[pickaxe_id]["cost"] > userinfo.coins:
        await message.send_error(msg, "You don't have enough coins for this pickaxe")
        return

    emojis = other.load_emojis(bot)
    sent_msg = await message.send_message(msg, f"Are you sure you want to buy a {pickaxes[pickaxe_id]['name']} for {pickaxes[pickaxe_id]['cost']} {emojis.coin}", title="Buying..",
        components=[[
            discord_components.Button(label="Confirm", style=discord_components.ButtonStyle.green),
            discord_components.Button(label="Cancel", style=discord_components.ButtonStyle.red)
        ]]
    )

    def button_check(interaction):
        if interaction.author != msg.author:
            return False

        if interaction.message != sent_msg:
            return False

        return True

    try:
        interaction = await bot.wait_for("button_click", timeout=120, check=button_check)
    except asyncio.TimeoutError:
        await message.timeout_response(sent_msg)
        return

    if interaction.component.label == "Cancel":
        await message.response_edit(sent_msg, interaction, sent_msg.embeds[0].description, title="Cancelled")
        return

    userinfo = user.load_user(msg.author.id, conn)

    if userinfo.pickaxe is not None:
        await message.response_send(sent_msg, interaction, "You already have a pickaxe equipped")
        return

    if pickaxes[pickaxe_id]["cost"] > userinfo.coins:
        await message.response_send(sent_msg, interaction, "You no longer have enough coins")
        return

    user.set_user_attr(msg.author.id, "coins", userinfo.coins - pickaxes[pickaxe_id]["cost"], conn, False)
    user.set_user_attr(msg.author.id, "pickaxe", abc.Pickaxe(
        pickaxes[pickaxe_id]["name"],
        pickaxes[pickaxe_id]["cost"],
        pickaxes[pickaxe_id]["speed"],
        pickaxes[pickaxe_id]["multiplier"]
    ).cvt_dict(), conn)

    await message.response_edit(sent_msg, interaction, f"You bought a {pickaxes[pickaxe_id]['name']} for {pickaxes[pickaxe_id]['cost']} {emojis.coin}", title="Bought")


async def _pickaxe_sell(bot, msg, conn):
    userinfo = user.load_user(msg.author.id, conn)

    if userinfo.pickaxe is None:
        await message.send_error(msg, "You don't have a pickaxe equipped")
        return

    sell_amount = round(userinfo.pickaxe.worth / 4)
    emojis = other.load_emojis(bot)
    sent_msg = await message.send_message(msg, f"Are you sure you want to sell your {userinfo.pickaxe.name} for {sell_amount} {emojis.coin}", title="Selling..",
        components=[[
            discord_components.Button(label="Confirm", style=discord_components.ButtonStyle.green),
            discord_components.Button(label="Cancel", style=discord_components.ButtonStyle.red)
        ]]
    )

    def button_check(interaction):
        if interaction.author != msg.author:
            return False

        if interaction.message != sent_msg:
            return False

        return True

    try:
        interaction = await bot.wait_for("button_click", timeout=120, check=button_check)
    except asyncio.TimeoutError:
        await message.timeout_response(sent_msg)
        return

    if interaction.component.label == "Cancel":
        await message.response_edit(sent_msg, interaction, sent_msg.embeds[0].description, title="Cancelled")
        return

    userinfo = user.load_user(msg.author.id, conn)

    if userinfo.pickaxe is None:
        await message.response_send(sent_msg, interaction, "You no longer have a pickaxe equipped")
        return

    sell_amount = round(userinfo.pickaxe.worth / 4)

    user.set_user_attr(msg.author.id, "coins", userinfo.coins + sell_amount, conn, False)
    user.set_user_attr(msg.author.id, "pickaxe", abc.Pickaxe(
        None, 0, 1, 1.0
    ).cvt_dict(), conn)

    await message.response_edit(sent_msg, interaction, f"You sold your {userinfo.pickaxe.name} for {sell_amount} {emojis.coin}", title="Sold")


async def _pickaxe_list(bot, msg):
    fields = []
    emojis = other.load_emojis(bot)

    for pickaxe in pickaxes.keys():
        fields.append([pickaxes[pickaxe]["name"], f"""ID: {pickaxe}
Cost: {pickaxes[pickaxe]['cost']} {emojis.coin}
Mining Speed: {pickaxes[pickaxe]['speed']}
Mining Multiplier: x{pickaxes[pickaxe]['multiplier']}"""])

    await message.send_message(msg, title="Pickaxes", fields=fields)