"""
Configuration Manager
"""

from pathlib import Path
import yaml


class Config:

    def __init__(self, filename="config/config.yaml"):

        self.filename = Path(filename)

        if not self.filename.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.filename}"
            )

        with open(self.filename, "r", encoding="utf-8") as file:
            self.data = yaml.safe_load(file)

    def get(self, section, default=None):
        return self.data.get(section, default)
