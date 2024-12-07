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
 
last_name_field = driver.find_element(By.ID, "primary_last_name")
last_name_field.send_keys(user_info['last_name'])

carleton_id_field = driver.find_element(By.ID, "primary_carleton_id")
carleton_id_field.send_keys(user_info['carleton_student_id'])

name_of_organization_field = driver.find_element(By.ID, "primary_position")
name_of_organization_field.send_keys("Carleton Computer Science Society")

role_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[1]/div/div[6]/div[1]/label/input")
role_field.click()

email_field = driver.find_element(By.ID, "primary_email")
email_field.send_keys(user_info['carleton_email'])

confirm_email_field = driver.find_element(By.ID, "primary_email_confirm")
confirm_email_field.send_keys(user_info['carleton_email'])

phone_number_field = driver.find_element(By.ID, "primary_phone")
phone_number_field.send_keys(user_info['phone_number'])

event_location_reserved_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[3]/div/div[10]/div[1]/label/input")
event_location_reserved_field.click()

expected_participants_field = driver.find_element(By.ID, "event_participants_number")
expected_participants_field.send_keys("20")

event_open_to_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[3]/div/div[12]/div/label[1]/input") #only selects students by default
event_open_to_field.click()

food_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[3]/div/div[13]/div[1]/label/input")
food_field.click()

health_card_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[3]/div/div[15]/div[1]/label/input")
health_card_field.click()

id_required_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[3]/div/div[16]/div[1]/label/input")
id_required_field.click()

minors_present_field =  driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[3]/div/div[17]/div[2]/label/input")
minors_present_field.click()

vip_speaker_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[3]/div/div[18]/div[1]/label/input")
vip_speaker_field.click()

alcohol_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[4]/div/div[1]/div[1]/label/input")
alcohol_field.click()

speakers_present_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[5]/div/div[1]/div[2]/label/input")
speakers_present_field.click()

volunteers_trained_first_aid_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[6]/div/div[1]/div[1]/label/input")
volunteers_trained_first_aid_field.click()

volunteers_know_nearest_hospital_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[6]/div/div[3]/div[2]/label/input")
volunteers_know_nearest_hospital_field.click()

evacuation_plan_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[6]/div/div[4]/div[2]/label/input")
evacuation_plan_field.click()

flames_or_dust_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[6]/div/div[5]/div[1]/label/input")
flames_or_dust_field.click()

crowd_control_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[7]/div/div[1]/div[2]/label/input")
crowd_control_field.click()

details_to_control_capacity_field = driver.find_element(By.ID, "safety_crowd_detail")
details_to_control_capacity_field.send_keys("The number of attendees will be limited to the recommended capacity of the room the event will take place in ")

safety_special_circumstances_field = driver.find_element(By.ID, "safety_special")
safety_special_circumstances_field.send_keys("None")

other_risks_safety_field = driver.find_element(By.ID, "safety_risk")
other_risks_safety_field.send_keys("None")

contracts_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[8]/div/div[1]/div[1]/label/input")
contracts_field.click()

insurance_coverage_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[8]/div/div[3]/div[1]/label/input")
insurance_coverage_field.click()

coverage_included_in_rental_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[8]/div/div[4]/div[3]/label/input")
coverage_included_in_rental_field.click()

certificate_of_insurance_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[8]/div/div[5]/div[3]/label/input")
certificate_of_insurance_field.click()

transportation_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[9]/div/div[1]/div[1]/label/input")
transportation_field.click()

out_of_province_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[10]/div/div[1]/div[1]/label/input")
out_of_province_field.click()

facilities_management_contracted_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[11]/div/div[1]/div[1]/label/input")
facilities_management_contracted_field.click()

volunteers_clean_up_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[11]/div/div[2]/div[2]/label/input")
volunteers_clean_up_field.click()

volunteers_clean_up_text_field = driver.find_element(By.ID, "fmp_cleanup_details")
volunteers_clean_up_text_field.send_keys("The event organizers and volunteers will clean up after the event")

event_setup_remain_overnight_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[11]/div/div[4]/div[1]/label/input")
event_setup_remain_overnight_field.click()

event_is_inclusive_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[12]/div/div[1]/div[2]/label/input")
event_is_inclusive_field.click()

risks_to_participants_field = driver.find_element(By.XPATH, "//*[@id='covidForm']/fieldset[12]/div/div[2]/div[1]/label/input")
risks_to_participants_field.click()

any_other_risks_field = driver.find_element(By.ID, "rights_other")
any_other_risks_field.send_keys("None")









