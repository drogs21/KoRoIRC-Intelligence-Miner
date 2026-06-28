"""
Coin command plugin
"""

from database import CoinDatabase
from providers.coingecko import CoinGecko


async def coin(bot, target, by, args):

    if len(args) == 0:
        await bot.message(target, "Usage: !coin <symbol>")
        return

    symbol = args[0].lower()

    db = CoinDatabase()
    coin_info = db.get(symbol)

    if coin_info is None:
        await bot.message(
            target,
            f"Unknown coin '{symbol}'. Use !coins to see supported coins."
        )
        return

    try:

        cg = CoinGecko()

        data = cg.get_coin(coin_info["id"])

        price = data["market_data"]["current_price"]["usd"]
        change = data["market_data"]["price_change_percentage_24h"]
        marketcap = data["market_data"]["market_cap"]["usd"]
        volume = data["market_data"]["total_volume"]["usd"]

        message = (
            f"{coin_info['name']} ({coin_info['symbol']}) | "
            f"Algo: {coin_info['algorithm']} | "
            f"Price: ${price:,.2f} | "
            f"24h: {change:.2f}% | "
            f"MCAP: ${marketcap:,.0f} | "
            f"VOL: ${volume:,.0f}"
        )

        await bot.message(target, message)

    except Exception as e:

        print(e)

        await bot.message(
            target,
            "Error retrieving data from CoinGecko."
        )
