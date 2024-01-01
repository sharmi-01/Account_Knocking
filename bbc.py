from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from colorama import Fore
from selenium.common.exceptions import TimeoutException


def sign_up(emails):

    chrome_options = Options()

    driver_path = ChromeDriverManager().install()

    service = Service(executable_path=driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        for email in emails:
            driver.get("https://account.bbc.com/auth?realm=%2F&clientId=Account&context=homepage&ptrt=https%3A%2F%2Fwww.bbc.com%2F&userOrigin=HOMEPAGE_GNL&isCasso=false&action=sign-in&redirectUri=https%3A%2F%2Fsession.bbc.com%2Fsession%2Fcallback%3Frealm%3D%2F&service=IdSignInService&nonce=5UCDlkyl-UQGkyOvEgRvx6Hd8xy7LqZOVIv0")

            email_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "user-identifier-input")))
            email_input.send_keys(email)

            sign_in_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "submit-button")))

            sign_in_button.click()

            time.sleep(4)

            try:

                error_message_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='form-message-general']/p[@class='sb-form-message__text']/span/span/a[@class='link']")))
                error_message = error_message_element.text
                print(Fore.YELLOW + f'This "{email}" doesn\'t exist in BBC news feed.')
            except TimeoutException:
                print(Fore.GREEN + f'This address is already linked to an existing account for {email}.')

    finally:
        driver.quit()


emails_to_check =['nagasharmilaperumal@gmail.com','nagasharmila.p2021cce@sece.ac.in']
sign_up(emails_to_check)
