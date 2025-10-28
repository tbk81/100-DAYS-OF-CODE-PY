import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


ACCOUNT_EMAIL = "user01@test.com"
ACCOUNT_PW = os.environ.get("SNACK_LIFT_PW")

endpoint = "https://appbrewery.github.io/gym/"

# Chrome and driver setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(endpoint)

# Log into website
wait = WebDriverWait(driver, 2)

login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

email_input = wait.until(ec.element_to_be_clickable((By.ID, "email-input")))
email_input.send_keys(ACCOUNT_EMAIL)

pw_input = wait.until(ec.element_to_be_clickable((By.ID, "password-input")))
pw_input.send_keys(ACCOUNT_PW)

submit_button = driver.find_element(By.ID, "submit-button")
submit_button.click()

# Wait for the schedule page to load
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

class_titles = driver.find_elements(By.CSS_SELECTOR, "h2")

for class_ in class_titles:
    print(class_.text)
