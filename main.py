from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os
import pickle

load_dotenv('credentials.env')

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

driver = webdriver.Chrome()


def save_cookies():
    # Save cookies to a file
    with open("cookies.pkl", "wb") as f:
        pickle.dump(driver.get_cookies(), f)
    print("Cookies saved successfully")


def load_cookies():
    # Load cookies from a file
    try:
        with open("cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)
        print("Cookies loaded successfully")
    except FileNotFoundError:
        print("No cookies found, starting a new session")


def main():
    login()
    search('Google Pixel')


def login():
    try:
        driver.get("https://jiji.ng")

        load_cookies()

        driver.refresh()

        # Wait for and click the registration button
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "h-flex-center"))
        )

        print('Sign in button found')
        sign_in_button.click()
        print('Sign in button clicked')

        # Wait for the overlay element and set its display to 'none'
        overlay_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "fw-fixed-background"))
        )
        driver.execute_script(
            "arguments[0].style.display = 'none';", overlay_element)
        print("Overlay element removed")

        # Wait and click on the email or phone button
        email_phone_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".h-width-100p.h-bold.fw-button.qa-fw-button.fw-button--type-success.fw-button--size-large"))  # Combined class names
        )
        print('Email or phone button found')
        email_phone_button.click()
        print('Email or phone button clicked')

        # Input the login credentials
        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "qa-login-field"))
        )
        email_field.send_keys(EMAIL)
        print("Email entered")

        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "qa-password-field"))
        )
        password_field.send_keys(PASSWORD)
        print("Password entered")

        save_cookies()

    except Exception as e:
        print(f"An error occured: {e}")


def search(query):
    # Perform search actions
    try:
        # Wait for and interact with the search bar
        search_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "multiselect__input"))
        )
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        print(f"Search query '{query}' entered")

    except Exception as e:
        print(f"An error occurred during search: {e}")


if __name__ == '__main__':
    main()