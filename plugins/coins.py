"""
Coins command plugin
"""

from database import CoinDatabase


async def coins(bot, target, by, args):

    db = CoinDatabase()

    items = []

    for key, coin in db.all().items():
        items.append(f"{coin['symbol']} ({key})")

    await bot.message(
        target,
        "Supported CPU coins: " + ", ".join(items)
    )
