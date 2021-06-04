# <--- General ---> #

help_ = {
    "desc": "Get a list of commands or details of a command",
    "usage": "help [category/command]",
    "args": {
        "category/command": "The category or command you want details of (Can be empty to get a list of categories)"
    }
}

ping = {
    "desc": "Get the latency of Talia",
    "usage": "ping",
    "args": {}
}

info = {
    "desc": "Get information about someone",
    "usage": "info [user]",
    "args": {
        "user": "The person you want to get information of (Can be empty to get your own)"
    }
}

stats = {
    "desc": "Get some cool stats about Talia",
    "usage": "stats",
    "args": {}
}

inventory = {
    "desc": "Get a list of items in someones inventory",
    "usage": "inventory [user]",
    "args": {
        "user": "The person you want to get the inventory of (Can be empty to get your own)"
    }
}

school = {
    "desc": "Get a higher education level",
    "usage": "school",
    "args": {}
}

box = {
    "desc": "Buy and open a mystery box",
    "usage": "box <operation> [box id]",
    "args": {
        "operation": "buy/list",
        "box id": "The box ID you want to buy (Only needed if buying)"
    }
}

leaderboard = {
    "desc": "See the leaderboard of a certain subject",
    "usage": "leaderboard <lb>",
    "args": {
        "lb": "The leaderboard that you want to see"
    }
}

company = {
    "desc": "Manage the company you're in",
    "usage": "company <operation> [company name/user]",
    "args": {
        "operation": "create/leave/invite/kick/disband/info",
        "company/user": "The company name if creating/getting info, or the user if inviting/kicking"
    }
}

showcase = {
    "desc": "Place an item from your inventory in your showcase box",
    "usage": "showcase <item/remove>",
    "args": {
        "item/remove": "The ID of the item in your inventory or \"remove\" to remove the item"
    }
}


# <--- Earning ---> #

job = {
    "desc": "Join, quit, or get a list of jobs",
    "usage": "job <operation> [job]",
    "args": {
        "operation": "join/quit/list",
        "job": "The job you want to join"
    }
}

work = {
    "desc": "Work at your job for coins and XP",
    "usage": "work",
    "args": {}
}

heist = {
    "desc": "Rob the bank to earn lots of money",
    "usage": "heist <contract>",
    "args": {
        "contract": "The ID of the heist contract in your inventory"
    }
}

invest = {
    "desc": "Invest coins to earn back more than you invested",
    "usage": "invest <amount> <time>",
    "args": {
        "amount": "The amount you want to invest",
        "time": "The time you want to invest for (hour, 8hour, day, week)"
    }
}

pickaxe = {
    "desc": "Buy, sell, or get a list of pickaxes",
    "usage": "pickaxe <operation> [pickaxe]",
    "args": {
        "operation": "buy/sell/list",
        "pickaxe": "The ID of pickaxe you want to buy"
    }
}

mine = {
    "desc": "Mine in the caverns with your pickaxe",
    "usage": "mine",
    "args": {}
}

hourly = {
    "desc": "Collect your hourly",
    "usage": "hourly",
    "args": {}
}

daily = {
    "desc": "Collect your daily",
    "usage": "daily",
    "args": {}
}


# <--- Gambling ---> #

coinflip = {
    "desc": "Flip a coin and bet on what side it will land on",
    "usage": "coinflip [side] [bet]",
    "args": {
        "side": "heads/tails",
        "bet": "The amount of coins you want to bet"
    }
}

dice = {
    "desc": "Roll a dice and bet on what side it will land on",
    "usage": "dice [side] [bet]",
    "args": {
        "side": "A number between 1-6",
        "bet": "The amount of coins you want to bet"
    }
}

blackjack = {
    "desc": "Play a game of blackjack",
    "usage": "blackjack [bet]",
    "args": {
        "bet": "The amount of coins you want to bet"
    }
}


# <--- Settings ---> #

prefix = {
    "desc": "Change the prefix for Talia for the server",
    "usage": "prefix <new prefix>",
    "args": {
        "new prefix": "The new prefix"
    }
}

channels = {
    "desc": "Enable or disable channels where commands can be run",
    "usage": "channels <operation> <channel>",
    "args": {
        "operation": "enable/disable",
        "channel": "The channel to enable or disable"
    }
}