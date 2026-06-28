"""
Ping command plugin.
"""


async def ping(bot, target, by, args):
    """
    Risponde al comando !ping
    """

    await bot.message(target, "PONG")
