from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
from colorama import Fore
from selenium.common.exceptions import TimeoutException


def sign_up(emails):

    chrome_options = Options()

    driver_path = ChromeDriverManager().install()

    service = Service(executable_path=driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        for email in emails:
            driver.get("https://www.spotify.com/in-en/signup/")

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(email)
            time.sleep(4)

            pyautogui.press('enter')

            try:
                error_message_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.Message-sc-15vkh7g-0.cdQMfn")))
                error_message = error_message_element.text
                print(f'{email}')

                print(Fore.GREEN + f'This address is already linked to an existing account.')
            except TimeoutException:
                print(Fore.YELLOW + f'This "{email}" doesn\'t exist in Spotify')

    finally:
        driver.quit()


emails_to_check = ['test@example.com', 'nagasharmilaperumal@gmail.com']
sign_up(emails_to_check)


