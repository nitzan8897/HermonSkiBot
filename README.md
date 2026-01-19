# Todos
- Make Railway use Shachar's proxy and send the HTTP request.

Currently the last commit isn't working because proxy problems so we work with the recent local development commit.

# Hermon Ski Alert Bot

A Telegram bot that monitors the Hermon ski resort ticket page and alerts you when skiing tickets become available.

## How it works

The bot checks the Hermon ticket purchase page for the text "לא נמצאו שוברים למכירה" (No vouchers found for sale). When this text is NOT present, it means tickets are available and you'll get an alert.

## Features

- **Automatic monitoring** - Checks every 5 minutes and alerts when tickets become available
- **Manual check** - Use `/status` command to check on demand

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Create Telegram bot

1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` and follow the instructions
3. Copy the bot token

### 3. Get your Chat ID

1. Message [@userinfobot](https://t.me/userinfobot) on Telegram
2. Copy your chat ID

### 4. Configure environment

Create a `.env` file:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

### 5. Run the bot

```bash
python main.py
```

## Commands

| Command | Description |
|---------|-------------|
| `/status` | Manually check if skiing is open |

## Project Structure

```
hermon-bot/
├── main.py          # Entry point, runs the bot and periodic checks
├── config.py        # Configuration and environment variables
├── scraper.py       # Selenium scraper for checking the website
├── telegram_bot.py  # Telegram bot handlers
├── requirements.txt # Python dependencies
└── .env             # Your credentials (not in git)
```

## Requirements

- Python 3.8+
- Chrome browser installed (for Selenium)
