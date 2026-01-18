import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import TELEGRAM_BOT_TOKEN, HERMON_URL
from scraper import check_hermon_tickets


def send_telegram_message(bot_token, chat_id, message):
    """Send a message to a specific chat."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"Error sending Telegram message: {e}")
        return False


async def status_command(update: Update, _context: ContextTypes.DEFAULT_TYPE):
    """Handle the /status command."""
    await update.message.reply_text("בודק לך על הסקי יזין")

    tickets_available = check_hermon_tickets()

    if tickets_available is None:
        await update.message.reply_text("שגיאה בבדיקה, נסה שוב")
    elif tickets_available:
        dates_str = ", ".join(d.strftime("%d/%m/%Y") for d in tickets_available)
        await update.message.reply_text(f"פתוח!!!! רוץ לקנות {HERMON_URL}\nמצאתי סקי-פסים בתאריכים:\n{dates_str}")
    else:
        await update.message.reply_text("סגור :(")


def create_bot_app():
    """Create and configure the Telegram bot application."""
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("status", status_command))
    return app
