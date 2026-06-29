# KoRoIRC-Intelligence-Miner

An IRC bot focused on **CPU Mining Intelligence**.

The project provides real-time cryptocurrency information, mining statistics, market analysis and CPU mining recommendations directly from IRC.

---

## Features

- IRC Bot
- Plugin-based architecture
- CoinGecko Market API
- SupportXMR Miner API
- YAML Configuration
- Market Cache
- Rig Cache
- CPU Mining Ranking
- Easy to extend

---

## Supported Coins

| Coin | Symbol | Algorithm |
|------|--------|-----------|
| Monero | XMR | RandomX |
| Salvium | SAL | RandomX |
| Zephyr Protocol | ZEPH | RandomX |
| Dero | DERO | AstroBWT |
| Quantum Resistant Ledger | QRL | RandomX |

---

## IRC Commands

| Command | Description |
|----------|-------------|
| !ping | Test bot connectivity |
| !coin xmr | Show information about a coin |
| !coins | List supported coins |
| !top | Show monitored market overview |
| !bestcpu | CPU Mining Intelligence ranking |
| !hashrate | Display current rig statistics |

---

## Current Features

- Live coin prices
- 24h market changes
- Market Cap
- Trading Volume
- SupportXMR integration
- Automatic cache updates
- CPU Mining Intelligence engine

---

## Installation

Clone the repository

```bash
git clone git@github.com:drogs21/KoRoIRC-Intelligence-Miner.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure

```
config/config.yaml
```

Run

```bash
python3 bot.py
```

---

## Project Structure

```
config/
core/
engine/
plugins/
providers/
services/

bot.py
requirements.txt
README.md
```

---

## Roadmap

### Completed

- [x] IRC Client
- [x] Plugin System
- [x] CoinGecko API
- [x] SupportXMR API
- [x] Market Cache
- [x] Rig Cache
- [x] CPU Mining Ranking

### Planned

- [ ] Mining Profit Calculator
- [ ] Difficulty Providers
- [ ] Network Hashrate
- [ ] Reward Estimation
- [ ] Automatic IRC Notifications
- [ ] GitHub Integration
- [ ] Web Dashboard
- [ ] Discord Bridge

---

## Philosophy

The goal of this project is **not** simply showing cryptocurrency prices.

The goal is to build an intelligent IRC assistant able to help CPU miners choose the most suitable cryptocurrency based on real mining data.

---

## Author

Developed by **KoRoIRC**

GitHub

https://github.com/drogs21

---

## License

MIT License
