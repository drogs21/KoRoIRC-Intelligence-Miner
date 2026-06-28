"""
IRC Client
"""

import asyncio
import pydle

from core.command_manager import CommandManager


class IRCClient(pydle.Client):

    def __init__(self, config):

        super().__init__(
            nickname=config["nickname"],
            username=config["username"],
            realname=config["realname"],
        )

        self.config = config
        self.command_manager = CommandManager()

    async def on_connect(self):
        print("[IRC] Connected")

        for channel in self.config["channels"]:
            await self.join(channel)

    async def on_join(self, channel, user):
        if user == self.nickname:
            print(f"[IRC] Joined {channel}")

    async def on_message(self, target, by, message):
        print(f"[{target}] <{by}> {message}")

        await self.command_manager.dispatch(
            self,
            target,
            by,
            message,
        )

    async def start(self):

        await self.connect(
            hostname=self.config["server"],
            port=self.config["port"],
            tls=self.config["ssl"],
        )

        # Mantiene viva l'applicazione senza avviare un secondo reader
        while self.connected:
            await asyncio.sleep(1)
