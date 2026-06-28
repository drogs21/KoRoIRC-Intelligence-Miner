"""
Application Core
"""

import asyncio

from rich.console import Console

from config import Config
from services.irc import IRCClient


class Application:

    def __init__(self):
        self.console = Console()
        self.config = Config()

    async def start(self):

        self.console.print("[green]Configuration loaded[/green]")

        irc = IRCClient(self.config.get("irc"))

        await irc.start()

    def run(self):
        asyncio.run(self.start())
