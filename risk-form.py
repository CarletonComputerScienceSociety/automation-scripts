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

def click_radio_button(xpath):
    button = driver.find_element(By.XPATH, xpath)
    button.click()

def fill_text_field(id, text):
    field = driver.find_element(By.ID, id)
    field.send_keys(text)

xpaths = {
    "role_field": "//*[@id='covidForm']/fieldset[1]/div/div[6]/div[1]/label/input",
    "event_location_reserved": "//*[@id='covidForm']/fieldset[3]/div/div[10]/div[1]/label/input",
    "event_open_to": "//*[@id='covidForm']/fieldset[3]/div/div[12]/div/label[1]/input",
    "food": "//*[@id='covidForm']/fieldset[3]/div/div[13]/div[1]/label/input",
    "health_card": "//*[@id='covidForm']/fieldset[3]/div/div[15]/div[1]/label/input",
    "id_required": "//*[@id='covidForm']/fieldset[3]/div/div[16]/div[1]/label/input",
    "minors_present": "//*[@id='covidForm']/fieldset[3]/div/div[17]/div[2]/label/input",
    "vip_speaker": "//*[@id='covidForm']/fieldset[3]/div/div[18]/div[1]/label/input",
    "alcohol": "//*[@id='covidForm']/fieldset[4]/div/div[1]/div[1]/label/input",
    "speakers_present": "//*[@id='covidForm']/fieldset[5]/div/div[1]/div[2]/label/input",
    "volunteers_trained_first_aid": "//*[@id='covidForm']/fieldset[6]/div/div[1]/div[1]/label/input",
    "volunteers_know_nearest_hospital": "//*[@id='covidForm']/fieldset[6]/div/div[3]/div[2]/label/input",
    "evacuation_plan": "//*[@id='covidForm']/fieldset[6]/div/div[4]/div[2]/label/input",
    "flames_or_dust": "//*[@id='covidForm']/fieldset[6]/div/div[5]/div[1]/label/input",
    "crowd_control": "//*[@id='covidForm']/fieldset[7]/div/div[1]/div[2]/label/input",
    "contracts": "//*[@id='covidForm']/fieldset[8]/div/div[1]/div[1]/label/input",
    "insurance_coverage": "//*[@id='covidForm']/fieldset[8]/div/div[3]/div[1]/label/input",
    "coverage_included_in_rental": "//*[@id='covidForm']/fieldset[8]/div/div[4]/div[3]/label/input",
    "certificate_of_insurance": "//*[@id='covidForm']/fieldset[8]/div/div[5]/div[3]/label/input",
    "transportation": "//*[@id='covidForm']/fieldset[9]/div/div[1]/div[1]/label/input",
    "out_of_province": "//*[@id='covidForm']/fieldset[10]/div/div[1]/div[1]/label/input",
    "facilities_management_contracted": "//*[@id='covidForm']/fieldset[11]/div/div[1]/div[1]/label/input",
    "volunteers_clean_up": "//*[@id='covidForm']/fieldset[11]/div/div[2]/div[2]/label/input",
    "event_setup_remain_overnight": "//*[@id='covidForm']/fieldset[11]/div/div[4]/div[1]/label/input",
    "event_is_inclusive": "//*[@id='covidForm']/fieldset[12]/div/div[1]/div[2]/label/input",
    "risks_to_participants": "//*[@id='covidForm']/fieldset[12]/div/div[2]/div[1]/label/input"
}

text_fields = {
    "primary_first_name": user_info['first_name'],
    "primary_last_name": user_info['last_name'],
    "primary_carleton_id": user_info['carleton_student_id'],
    "primary_position": "Carleton Computer Science Society",
    "primary_email": user_info['carleton_email'],
    "primary_email_confirm": user_info['carleton_email'],
    "primary_phone": user_info['phone_number'],
    "event_participants_number": "20",
    "safety_crowd_detail": "The number of attendees will be limited to the recommended capacity of the room the event will take place in",
    "safety_special": "None",
    "safety_risk": "None",
    "fmp_cleanup_details": "The event organizers and volunteers will clean up after the event",
    "rights_other": "None"
}

for key in xpaths:
    click_radio_button(xpaths[key])

for id, text in text_fields.items():
    fill_text_field(id, text)