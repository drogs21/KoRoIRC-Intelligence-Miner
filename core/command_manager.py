"""
Command Manager
"""

from plugins.ping import ping
from plugins.coin import coin
from plugins.coins import coins


class CommandManager:

    def __init__(self):

        self.commands = {
            "ping": ping,
            "coin": coin,
            "coins": coins,
        }

    async def dispatch(self, bot, target, by, message):

        if not message.startswith("!"):
            return

        parts = message[1:].split()

        if not parts:
            return

        command = parts[0].lower()
        args = parts[1:]

        handler = self.commands.get(command)

        if handler:
            await handler(bot, target, by, args)
