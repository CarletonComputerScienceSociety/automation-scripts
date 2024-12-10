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

driver.get("https://carleton.ca/scs/student-clubs-and-societies-room-booking-request-form/")

first_name_field = driver.find_element(By.ID, "input_47_61")
first_name_field.send_keys(user_info['first_name'])

last_name_field = driver.find_element(By.ID, "input_47_62")
last_name_field.send_keys(user_info['last_name'])

email_field = driver.find_element(By.ID, "input_47_41")
email_field.send_keys(user_info['carleton_email'])

confirm_email_field = driver.find_element(By.ID, "input_47_41_2")
confirm_email_field.send_keys(user_info['carleton_email'])

carleton_id_field = driver.find_element(By.ID, "input_47_57")
carleton_id_field.send_keys(user_info['carleton_student_id'])

name_of_club_field = driver.find_element(By.ID, "choice_47_59_3")
name_of_club_field.click() #refactor variable name later

if (user_info['position_in_society'] == 'President'):
    position_in_society_field = driver.find_element(By.ID, "choice_47_49_0")
    position_in_society_field.click()

else:
    position_in_society_field_button = driver.find_element(By.ID, "choice_47_49_3")
    position_in_society_field_button.click()

    position_in_society_field_text = driver.find_element(By.ID, "input_47_49_other")
    position_in_society_field_text.send_keys(user_info['position_in_society']) #refactor variable name later

swipe_access_names_field = driver.find_element(By.ID, "input_47_53")
swipe_access_names_field.send_keys(user_info['first_name'] + ' ' + user_info['last_name'])

number_of_attendees_field = driver.find_element(By.ID, "input_47_54")
number_of_attendees_field.send_keys("30") #hardcoded here, can be modified on the page if needed

food_served_field = driver.find_element(By.ID, "choice_47_55_1")
food_served_field.click() #refactor variable name later

consent_field = driver.find_element(By.ID, "input_47_42_1")
consent_field.click() #refactor variable name later





