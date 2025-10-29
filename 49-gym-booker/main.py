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

# Find all class cards
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday
    if "Tue" in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            button.click()

            print(f"✓ Booked: {class_name} on {day_title}")


# ==================== NOTES AND DEV ==================== #
# p → Match a <p> (paragraph) element.
# [id^='class-time-'] → Match only if its id starts with "class-time-".

# class_date = driver.find_elements(By.CSS_SELECTOR, "h2")
# class_titles = driver.find_elements(By.CSS_SELECTOR, "h3")
# class_times = driver.find_elements(By.CSS_SELECTOR, "p[id^='class-time-']")
# print(len(class_titles))
# print(len(class_times))

# for date in class_date:
#     if "Tue" in date.text:
#         print(date.text)

# for title in class_titles:
#     print(title.text)
#
# for time in class_times:
#     print(time.text)


