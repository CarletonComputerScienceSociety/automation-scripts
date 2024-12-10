from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import json

def click_radio_button(id):
    button = driver.find_element(By.ID, id)
    button.click()

def fill_text_field(id, text):
    field = driver.find_element(By.ID, id)
    field.send_keys(text)

with open('config.json') as f:
    user_info = json.load(f)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://carleton.ca/scs/student-clubs-and-societies-room-booking-request-form/")

text_field_ids = { # id: value # field
    "input_47_61": user_info['first_name'],  # First Name
    "input_47_62": user_info['last_name'],   # Last Name
    "input_47_41": user_info['carleton_email'],  # Email
    "input_47_41_2": user_info['carleton_email'],  # Confirm Email
    "input_47_57": user_info['carleton_student_id'],  # Carleton ID
    "input_47_53": user_info['first_name'] + ' ' + user_info['last_name'],  # Swipe Access Names
    "input_47_54": "30",  # Number of Attendees
}

radio_button_ids = { # id: field
    "choice_47_59_3": "Name of Club",
    "choice_47_55_1": "Food Served",
    "input_47_42_1": "Consent"
}

for id, text in text_field_ids.items():
    fill_text_field(id, text)

for id in radio_button_ids.keys():
    click_radio_button(id)

# Position in Society handled separately
if user_info['position_in_society'] == 'President':
    click_radio_button("choice_47_49_0")
else:
    click_radio_button("choice_47_49_3")
    fill_text_field("input_47_49_other", user_info['position_in_society'])






