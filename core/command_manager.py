"""
Command Manager
"""

from plugins.ping import ping


class CommandManager:

    def __init__(self):
        self.commands = {
            "ping": ping,
        }

    async def dispatch(self, bot, target, by, message):

        if not message.startswith("!"):
            return

        parts = message[1:].split()

        if not parts:
            return

        command = parts[0].lower()
        args = parts[1:]

        if command not in self.commands:
            return

        await self.commands[command](bot, target, by, args)
