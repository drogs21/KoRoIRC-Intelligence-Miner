"""
Coin command plugin
"""

from providers.coingecko import CoinGecko


async def coin(bot, target, by, args):

    if len(args) == 0:
        await bot.message(target, "Usage: !coin <coin>")
        return

    coin_id = args[0].lower()

    try:

        cg = CoinGecko()
        data = cg.get_coin(coin_id)

        name = data["name"]
        symbol = data["symbol"].upper()

        price = data["market_data"]["current_price"]["usd"]

        change = data["market_data"]["price_change_percentage_24h"]

        marketcap = data["market_data"]["market_cap"]["usd"]

        volume = data["market_data"]["total_volume"]["usd"]

        await bot.message(
            target,
            f"{name} ({symbol}) | "
            f"Price: ${price:,.2f} | "
            f"24h: {change:.2f}% | "
            f"MCAP: ${marketcap:,.0f} | "
            f"VOL: ${volume:,.0f}"
        )

    except Exception:
        await bot.message(target, "Coin not found.")
