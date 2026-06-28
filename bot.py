#!/usr/bin/env python3
"""
CPU Mining Intelligence
Main Entry Point
"""

from rich.console import Console
from rich.panel import Panel

from core.application import Application

console = Console()


def banner():
    """Visualizza il banner."""

    console.print()

    console.print(
        Panel.fit(
            "[bold cyan]CPU Mining Intelligence[/bold cyan]\n"
            "[green]Version 0.1.0[/green]",
            border_style="blue"
        )
    )

    console.print()


def main():

    banner()

    app = Application()

    app.run()


if __name__ == "__main__":
    main()
