import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os
from login import login  # Corrected import statement

# Load environment variables
load_dotenv('credentials.env')

driver = webdriver.Chrome()


def main():
    search('Google Pixel')


def search(query):
    try:
        driver.get("https://jiji.ng")

        # Search for the query
        search_box = driver.find_element(By.CLASS_NAME, "multiselect__input")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        print(f"Search query '{query}' entered")

        time.sleep(10)

        # Click the first result
        first_result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".b-list-advert-base.qa-advert-list-item.b-list-advert-base--vip.b-list-advert-base--gallery"))
        )
        first_result.click()
        print("First search result clicked")

        # Wait for the product page to load by waiting for the price element
        # WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located(
        #         (By.CLASS_NAME, "qa-advert-price"))
        # )
        # print("Product page loaded")

        # Click the 'Show Contact' button
        show_contact_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".qa-show-contact.cy-show-contact.js-show-contact.b-show-contact.b-advert-card-wrapper__buttons-item"))
        )
        show_contact_button.click()
        print('Show contact button clicked')

        # Now perform login (this should handle the login modal)
        login(driver)
        print("Login performed")

        # Wait for the page to refresh after login and click 'Show Contact' again
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".qa-show-contact.cy-show-contact.js-show-contact.b-show-contact.b-advert-card-wrapper__buttons-item"))
        ).click()
        print('Show contact button clicked again after login')

        time.sleep(5)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".qa-show-contact.cy-show-contact.js-show-contact.b-show-contact.b-advert-card-wrapper__buttons-item"))
        ).click()
        print('Show contact button clicked again after login')

        # Extract the product details
        product_name = driver.find_element(
            By.CLASS_NAME, "qa-advert-title").text
        product_price = driver.find_element(
            By.CLASS_NAME, "qa-advert-price-view-title").text
        seller_name = driver.find_element(
            By.CLASS_NAME, "b-seller-block__name").text

        # Extract all phone numbers
        phone_elements = driver.find_elements(
            By.CLASS_NAME, "b-show-contacts-popover-item__phone")
        phone_numbers = [phone.text for phone in phone_elements]
        print(f"Phone Numbers: {phone_numbers}")

        # Print extracted details
        print(f"Product Name: {product_name}")
        print(f"Product Price: {product_price}")
        print(f"Seller Name: {seller_name}")

        # Store the extracted data in a dictionary
        product_data = {
            "Product Name": product_name,
            "Product Price": product_price,
            "Seller Name": seller_name,
            "Phone Numbers": phone_numbers
        }

        # Save the data into a JSON file
        with open('product_data.json', 'w') as json_file:
            json.dump(product_data, json_file, indent=4)
        print("Product details saved to product_data.json")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
