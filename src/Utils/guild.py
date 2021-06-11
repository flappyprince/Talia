"""
Talia Discord Bot
GNU General Public License v3.0
guild.py (Utils)

Utilities for the management of guilds within the database
"""
import json
from Utils import abc


def load_guild(guild_id, conn):
    """
    Loads a guild from the database

    1. Looks for the guild with a certain ID (Based off of discord ID)
    2. Takes the returned list and assigns each value to it's spot in a guild object
    3. Attributes stored in a class use the json library for serialization
     and get stored in a dictionary until converted
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM guilds WHERE id = ?", (guild_id,))
    guildinfo = cur.fetchone()
    
    if guildinfo is None:
        return None
    
    new_guild = abc.Guild(guildinfo[0])
    new_guild.prefix = guildinfo[1]
    new_guild.disabled_channels = json.loads(guildinfo[2])
    new_guild.aliases = json.loads(guildinfo[3])
    new_guild.shop = json.loads(guildinfo[4])
    
    return new_guild


def write_guild(obj, conn, write=True):
    """
    Creates a new guild entry in the database

    1. Creates a new cursor and inserts the guild into the database
    2. Commits if the write parameter is true
    """
    cur = conn.cursor()
    cur.execute("INSERT INTO guilds VALUES (?, ?, ?, ?, ?)", (
        obj.id,
        obj.prefix,
        json.dumps(obj.disabled_channels),
        json.dumps(obj.aliases),
        json.dumps(obj.shop)
    ))
    
    if write:
        conn.commit()


def set_guild_attr(guild_id, attr, val, conn, write=True):
    """
    Sets a certain attribute of a guild in the database

    1. Checks for the value type and converts it to a value
     that sqlite can understand
    2. Creates a new cursor and sets the value
    3. Commits if the write parameter is true
    """
    if type(val) == bool:
        val = str(val)
    elif type(val) == list or type(val) == dict:
        val = json.dumps(val)
    
    cur = conn.cursor()
    cur.execute(f"UPDATE guilds SET {attr} = ? WHERE id = ?", (val, guild_id))
    
    if write:
        conn.commit()


def load_guild_prefix(guild_id, conn):
    """
    Quickly loads a guild's command prefix

    1. Creates a new cursor and grabs the prefix
    2. Returns just the prefix
    """
    cur = conn.cursor()
    cur.execute("SELECT prefix FROM guilds WHERE id = ?", (guild_id,))
    guild_prefix = cur.fetchone()

    if guild_prefix is None:
        return "t!"

    return guild_prefix[0]