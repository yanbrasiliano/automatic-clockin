from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import time
import argparse

# Argument parser setup
parser = argparse.ArgumentParser(description="Automate login and point registration.")
parser.add_argument('--screenshot', action='store_true', help="Take a screenshot after logging in without registering the point.")
args = parser.parse_args()

# Load environment variables from .env file
load_dotenv()

# Get credentials from .env file
login_value = os.getenv('LOGIN')
password_value = os.getenv('PASSWORD')
url = os.getenv('URL')
path = os.getenv('SCREENSHOT_PATH')

# Selenium configuration
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Start the browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

try:
    # Access the site
    driver.get(url)

    time.sleep(3)

    # Use JavaScript to set the login field value
    driver.execute_script(f"document.getElementById('Login2').value = '{login_value}';")
    print(f"Login inserted via JavaScript: {login_value}")

    # Check if the login was inserted
    login_field = driver.find_element(By.ID, 'Login2')
    print(f"Login field value after insertion: {login_field.get_attribute('value')}")

    # Use JavaScript to set the password field value
    driver.execute_script(f"document.getElementById('Pass2').value = '{password_value}';")
    print(f"Password inserted via JavaScript: {password_value}")

    # Check if the password was inserted
    password_field = driver.find_element(By.ID, 'Pass2')
    print(f"Password field value after insertion: {password_field.get_attribute('value')}")

    # Take a screenshot after filling in the fields
    driver.save_screenshot(os.path.join(path, 'screenshot_after_js.png'))

    # Submit the form using JavaScript
    driver.execute_script("document.querySelector('button[type=submit]').click();")

    # Wait for the login to be processed and the next page to load
    time.sleep(3)

    # Take a screenshot after logging in
    driver.save_screenshot(os.path.join(path, 'screenshot_after_login.png'))

    if not args.screenshot:
        # Wait until the "REGISTER POINT" button is present and visible
        register_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'btn-registrar'))
        )
        register_button.click()
        print("REGISTER POINT button clicked.")

        time.sleep(3)

        driver.save_screenshot(os.path.join(path, 'screenshot_after_register.png'))

finally:
    # Close the browser
    driver.quit()

print("Screenshot saved as 'screenshot_after_js.png' and 'screenshot_after_login.png'")
if not args.screenshot:
    print("Screenshot saved as 'screenshot_after_register.png'")
