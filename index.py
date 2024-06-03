from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv()

# Get credentials from .env file
login_value = os.getenv('LOGIN')
password_value = os.getenv('PASSWORD')
url = os.getenv('URL')

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
    driver.save_screenshot('screenshot_after_js.png')

    # Submit the form using JavaScript
    driver.execute_script("document.querySelector('button[type=submit]').click();")

    # Wait for the login to be processed and the next page to load
    time.sleep(3)

    # Take a screenshot of the page after login
    driver.save_screenshot('screenshot_after_submit.png')

    # Wait until the "REGISTER POINT" button is present and visible
    register_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'btn-registrar'))
    )
    register_button.click()
    print("REGISTER POINT button clicked.")

    time.sleep(3)

    driver.save_screenshot('screenshot_after_register.png')

finally:
    # Close the browser
    driver.quit()

print("Screenshot saved as 'screenshot_after_js.png', 'screenshot_after_submit.png', and 'screenshot_after_register.png'")
