import os
from dotenv import load_dotenv

load_dotenv()

HERMON_URL = "https://hermon.presglobal.store/ski"
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
CHECK_INTERVAL = 300  # Check every 5 minutes
PROXY_URL = os.getenv("PROXY_URL")  # Optional: http://user:pass@host:port
