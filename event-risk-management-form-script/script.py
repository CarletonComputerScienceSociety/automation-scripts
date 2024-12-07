from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import json

with open('config.json') as f:
    user_info = json.load(f)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://stuapps.carleton.ca/sarms/event-risk/in-person")

first_name_field = driver.find_element(By.ID, "primary_first_name")
first_name_field.send_keys(user_info['first_name'])