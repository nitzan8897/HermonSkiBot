import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from config import HERMON_URL, NO_TICKETS_TEXT


def get_driver():
    """Create a headless Chrome driver."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=options)


def check_hermon_tickets():
    """Check if tickets are available on the Hermon website."""
    driver = None
    try:
        driver = get_driver()
        driver.get(HERMON_URL)

        # Wait for page to load (wait up to 15 seconds for body to be present)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Give extra time for dynamic content to load
        time.sleep(5)

        page_text = driver.page_source
        print("Page loaded, checking for tickets...")

        if NO_TICKETS_TEXT in page_text:
            return False  # No tickets available
        else:
            return True   # Tickets might be available!

    except Exception as e:
        print(f"Error checking website: {e}")
        return None
    finally:
        if driver:
            driver.quit()
