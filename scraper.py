import requests
import random
import string
from datetime import datetime

API_URL = "https://hermon.presglobal.store/api/system-vouchers/byDate"

# Ski ticket voucher IDs
SKI_VOUCHER_IDS = {77, 80}


def generate_random_token(length=32):
    """Generate a random recaptcha token."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def check_hermon_tickets():
    """Check if ski tickets are available via the API."""
    try:
        token = generate_random_token()
        url = f"{API_URL}?recaptchaToken={token}"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()

        print("API response received, checking vouchers...")

        today = datetime.now().date()
        dates = data.get("Dates", [])
        found_dates = []

        for date_entry in dates:
            date_str = date_entry.get("Date", "")
            # Parse the date (format: "2025-01-19T00:00:00")
            try:
                entry_date = datetime.fromisoformat(date_str.replace("Z", "")).date()
            except ValueError:
                continue

            # Only check future dates
            if entry_date < today:
                continue

            vouchers = date_entry.get("Vouchers", [])
            for voucher in vouchers:
                voucher_id = voucher.get("SystemVoucherId")
                voucher_name = voucher.get("Name", "Unknown")

                if voucher_id in SKI_VOUCHER_IDS:
                    print(f"SKI TICKET FOUND! Date: {entry_date}, Voucher ID: {voucher_id} - {voucher_name}")
                    if entry_date not in found_dates:
                        found_dates.append(entry_date)

        if found_dates:
            return found_dates

        print("No ski tickets found in future dates (looking for IDs 77, 80)")
        return False

    except requests.RequestException as e:
        print(f"Error checking API: {e}")
        return None
