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
            driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Feu.primevideo.com%2Fregion%2Feu%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_t%3Dsg45dnPiqyhyTdJwB4cvkU03GHc08Y_wbpvIis2YfBc20AAAAAQAAAABlkTw7cmF3AAAAAPgWC9WfHH8iB-olH_E9xQ%26location%3D%2Fregion%2Feu%2F%3Fref_%253Datv_auth_pre&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&accountStatusPolicy=P1&openid.assoc_handle=amzn_prime_video_sso_in&openid.mode=checkid_setup&siteState=258-8435775-3084124&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

            email_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ap_email")))
            email_input.send_keys(email)

            continue_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "continue")))
            continue_button.click()

            time.sleep(4)

            try:
                error_message_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='auth-error-message-box']")))
                error_message = error_message_element.text
                print(Fore.YELLOW + f'This "{email}" doesn\'t exist in amazon prime')
            except TimeoutException:
                print(Fore.GREEN + f'This address is already linked to an existing account for {email}.')

    finally:
        driver.quit()


emails_to_check = ['nagasharmilaperumal@gmail.com','nagasharmila.p2021cce@sece.ac.in']
sign_up(emails_to_check)

