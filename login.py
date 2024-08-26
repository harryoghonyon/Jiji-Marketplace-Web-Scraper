from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv('credentials.env')

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def login(driver):
    try:
        # Remove the overlay
        overlay_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "fw-fixed-background"))
        )
        driver.execute_script(
            "arguments[0].style.display = 'none';", overlay_element)

        # Click the email or phone button
        email_phone_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, ".h-width-100p.h-bold.fw-button.qa-fw-button.fw-button--type-success.fw-button--size-large"
            ))
        )
        email_phone_button.click()

        # Enter the login credentials
        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "qa-login-field"))
        )
        email_field.send_keys(EMAIL)

        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "qa-password-field"))
        )
        password_field.send_keys(PASSWORD)

        # Click the sign-in button
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.CLASS_NAME, "h-width-100p.h-bold.qa-login-submit.fw-button.qa-fw-button.fw-button--type-success.fw-button--size-large"
            ))
        )
        sign_in_button.click()
        print("Sign-in button clicked")

        # Wait for the page to refresh indicating login success
        # Adjust the sleep duration based on how long it typically takes to log in
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred during login: {e}")
