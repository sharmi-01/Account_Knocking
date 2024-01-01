from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
from colorama import Fore, Back, Style
from selenium.common.exceptions import TimeoutException


def sign_up(emails):

    chrome_options = Options()

    driver_path = ChromeDriverManager().install()

    service = Service(executable_path=driver_path)

    for email in emails:

        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            driver.get("https://www.quora.com")

            try:
                button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "q-click-wrapper qu-active--bg--darken qu-mt--small qu-borderRadius--pill qu-alignItems--center qu-justifyContent--center qu-whiteSpace--nowrap qu-userSelect--none qu-display--flex qu-tapHighlight--white qu-textAlign--center qu-cursor--pointer qu-hover--bg--darken ClickWrapper___StyledClickWrapperBox-zoqi4f-0 iyYUZT base___StyledClickWrapper-lx6eke-1 cdVMwV ") and contains(. , "Sign up with email")]')))
                button.click()
            except TimeoutException:
                print("Button not found within the given time.")

            try:

                time.sleep(5)

                while True:
                    try:
                        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
                        email_input.send_keys(email)

                        pyautogui.press('enter')
                        break
                    except TimeoutException:
                        print("Email input field not found, retrying...")
                        time.sleep(1)

            except TimeoutException:
                print("Email input field not found within the given time.")

            try:
                error_message_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.q-text.qu-dynamicFontSize--small.qu-color--red_error")))
                error_message = error_message_element.text

                expected_error_message = "Account already exists with that e-mail address"

                assert error_message == expected_error_message, f"Expected '{expected_error_message}' but got '{error_message}'"

            except TimeoutException:
                error_message = False

            if error_message:
                print(Fore.GREEN + f'This address is already linked to an existing account.')
            else:
                print(Fore.YELLOW + f'This "{email}" doesn\'t exist in Quora')

        finally:
            driver.quit()


emails_to_check = ['rayonprogramming@gmail.com', 'nagasharmilaperumal@gmail.com']
sign_up(emails_to_check)
