#!/usr/bin/python3

from os import getenv
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import json 
from selenium.webdriver.chrome.options import Options

password_env = getenv("LINKEDIN_PWS")
if password_env is None:
    raise ValueError("Password not found in enviroment")

username_env = getenv("LINKEDIN_USER")
if username_env is None:
    raise ValueError("User not found in enviroment")

linkedin_urls = "https://www.linkedin.com/in/juan-gago-79648b64/"

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

wait = WebDriverWait(driver, 15)
driver.get('https://www.linkedin.com')
print(driver.title)
username = driver.find_element(By.ID, 'session_key')
username.send_keys(username_env)
password = driver.find_element(By.ID, 'session_password')
password.send_keys(password_env)
log_in_button = driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-button')
log_in_button.click()


driver.get(linkedin_urls)
name_xpath = "//h1[@class='text-heading-xlarge inline t-24 v-align-middle break-words']"
condition_name = EC.presence_of_element_located((By.XPATH, name_xpath))

name = wait.until(condition_name).text
print(name)

driver.execute_script("window.scrollBy(0, 1200)","")

xp_xpath_title = "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[4]/div[3]/ul/li/div/div[2]/div/div/div/span/span[1]"
condition_xp_title =  EC.presence_of_element_located((By.XPATH, xp_xpath_title))
experience = wait.until(condition_xp_title)
experience = experience.find_elements(By.XPATH, xp_xpath_title)
xp_title = [x.get_attribute("textContent") for x in experience]
print(xp_title)
xp_xpath_company = "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[4]/div[3]/ul/li/div/div[2]/div/div/div/span/span[1]"
#xp_xpath_company = "/html/body/main/section[1]/div/section/section[3]/div/ul/li/div/h4/a"
condition_xp_company = EC.presence_of_element_located((By.XPATH, xp_xpath_company))
companies = wait.until(condition_xp_company)
companies = companies.find_elements(By.XPATH, xp_xpath_company)
xp_company = [x.get_attribute("innerText") for x in companies]
print(xp_company)

driver.close()


