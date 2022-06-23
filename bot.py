#!/usr/bin/python3

import csv
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

data = {}

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://www.linkedin.com')
print("titulo: " + driver.title)
username = driver.find_element(By.ID, 'session_key')
username.send_keys("lau.manu2@gmail.com")
password = driver.find_element(By.ID, 'session_password')
password.send_keys("16Junioo")
log_in_button = driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-button')
log_in_button.click()

linkedin_urls = ["https://www.linkedin.com/in/juan-gago-79648b64/"]
titulo_puesto=[]
empresa=[]
fecha_trabajo=[]
universidad=[]
carrera=[]

driver.get("https://www.linkedin.com/in/juan-gago-79648b64/")
name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//h1[@class='text-heading-xlarge inline t-24 v-align-middle break-words']"))).text
print(name)
driver.execute_script("window.scrollBy(0, 1200)","")

experiencia = driver.find_elements(By.XPATH,"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[4]/div[3]/ul")
#experiencia = driver.find_elements(By.ARIA-HIDDEN, "true")
for my_href in experiencia :
    print(my_href.text)
 

"""texto_exp = experiencia.find_elements(By.XPATH, "//h3[@class='pvs-list ph5 display-flex flex-row flex-wrap']")
for titulo in texto_exp:
   titulo_puesto.append(titulo.text)
print(texto_exp)"""
driver.close()


