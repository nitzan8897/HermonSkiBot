import time
import threading

from config import HERMON_URL, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, CHECK_INTERVAL
from scraper import check_hermon_tickets
from telegram_bot import send_telegram_message, create_bot_app


def run_periodic_check():
    """Run periodic checks in background."""
    print("Starting periodic check...")
    while True:
        tickets_available = check_hermon_tickets()

        if tickets_available is None:
            print("Could not check website, will retry...")
        elif tickets_available:
            dates_str = ", ".join(d.strftime("%d/%m/%Y") for d in tickets_available)
            message = f"פתוח!!!! רוץ לקנות {HERMON_URL}\nמצאתי סקי-פסים בתאריכים:\n{dates_str}"
            send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, message)
            print("TICKETS AVAILABLE! Alert sent.")
        else:
            print("No tickets yet")

        time.sleep(CHECK_INTERVAL)


def main():
    """Main function."""
    print("Hermon Ski Alert Bot Started")
    print(f"Checking {HERMON_URL} every {CHECK_INTERVAL} seconds")
    print("-" * 50)

    # Start periodic check in background thread
    check_thread = threading.Thread(target=run_periodic_check, daemon=True)
    check_thread.start()

    # Start Telegram bot
    app = create_bot_app()
    print("Bot is running. Use /status to check manually.")
    app.run_polling()


if __name__ == "__main__":
    main()
