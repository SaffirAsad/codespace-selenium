from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time

URL = 'https://www.linkedin.com/checkpoint/rm/sign-in-another-account'
options = Options()
options.add_argument('--headless')
##options.add_argument('--disable-gpu')  # Last I checked this was necessary.
print("browser Starting..")
browser = webdriver.Chrome(executable_path=chromedriver_binary.chromedriver_filename,
                           options = options)
print("browser Started.")

browser.get(URL)
time.sleep(5)
print("browser Started url fetshed!.\n")
body = browser.find_element(By.CSS_SELECTOR , "body")
username = browser.find_element(By.ID,"username")
username.send_keys("saffirAsad@gmail.com");
password = browser.find_element(By.ID,"password")
password.send_keys("");
time.sleep(5)
body.screenshot("a.png")
time.sleep(5)
browser.close()
