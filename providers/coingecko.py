"""
CoinGecko Provider
"""

import requests


class CoinGecko:

    BASE_URL = "https://api.coingecko.com/api/v3"

    def get_coin(self, coin_id):

        url = f"{self.BASE_URL}/coins/{coin_id}"

        response = requests.get(
            url,
            params={
                "localization": "false",
                "tickers": "false",
                "market_data": "true",
                "community_data": "false",
                "developer_data": "false",
                "sparkline": "false"
            },
            timeout=10
        )

        response.raise_for_status()

        return response.json()
