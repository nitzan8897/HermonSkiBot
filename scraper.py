import time
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from config import HERMON_URL, NO_TICKETS_TEXT


def get_driver():
    """Create an undetected Chrome driver."""
    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    return uc.Chrome(options=options, browser_executable_path="/usr/bin/google-chrome")


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

        page_body = driver.find_element(By.TAG_NAME, "body").text
        print("Page loaded, checking for tickets...")
        print(f"Page body text (first 500 chars): {page_body[:500]}")

        if NO_TICKETS_TEXT in page_body:
            return False  # No tickets available
        else:
            print(f"Looking for: '{NO_TICKETS_TEXT}'")
            print(f"Not found in page body")
            return True   # Tickets might be available!

    except Exception as e:
        print(f"Error checking website: {e}")
        return None
    finally:
        if driver:
            driver.quit()
