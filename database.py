"""
CPU Coin Registry
"""

import yaml


class CoinDatabase:

    def __init__(self):

        with open("data/coins.yaml", "r") as fp:
            self.data = yaml.safe_load(fp)

    def get(self, symbol):

        symbol = symbol.lower()

        return self.data["coins"].get(symbol)

    def all(self):

        return self.data["coins"]
