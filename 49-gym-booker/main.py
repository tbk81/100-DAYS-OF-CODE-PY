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

book_num = 0
waitlist_num = 0
already_booked_waitlisted = 0
processed_classes = []

# Find all class cards
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    # Get the day title from the parent day group
    day_title = day_group.find_element(By.TAG_NAME, "h2").text
    # Gets the times of the class cards
    time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text

    # Check if this is a Tuesday
    if "Tue" in day_title or "Thu" in day_title:
        if "6:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            # Find the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            # Check if the class was waitlisted
            if button.text == "Waitlisted":
                already_booked_waitlisted += 1
                print(f"Already on the waitlist: {class_name} on {day_title}")
            elif button.text == "Booked":
                already_booked_waitlisted += 1
                print(f"Already booked: {class_name} on {day_title}")
            elif button.text == "Join Waitlist":
                button.click()
                waitlist_num += 1
                print(f"Joined waitlist for: {class_name} on {day_title}")
            else:
                button.click()
                book_num += 1
                print(f"Booked: {class_name} on {day_title}")
total = book_num + waitlist_num + already_booked_waitlisted
print(f"--- Booking Summary ---\nClasses booked: {book_num}\nWaitlists joined: {waitlist_num}\n"
      f"Already booked/waitlisted: {already_booked_waitlisted}\n"
      f"Total classes processed: {total}")


total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

# Navigate to My Bookings page
my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
my_bookings_link.click()

# Wait for My Bookings page to load
wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

# Count all Tuesday/Thursday 6pm bookings
verified_count = 0

# Find ALL booking cards (both confirmed and waitlist)
all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        # Check if it's a Tuesday or Thursday 6pm class
        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        # Skip if no "When:" text found (not a booking card)
        pass

# Simple comparison
print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")




# ======================================== NOTES AND DEV ======================================== #
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
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# Import exceptions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import time

# Create Chrome Profile and create account manually. Put YOUR email and password here:
ACCOUNT_EMAIL = "angela@test.com"
ACCOUNT_PASSWORD = "superSecretTestPassword"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
# Keep the browser open if the script finishes or crashes.
# If True, you need to *manually* QUIT Chrome before you re-run the script.
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)

driver.get(GYM_URL)

# ----------------  Step 9: Network Resilience ----------------

# Simple retry wrapper
def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)

# Function to perform entire login process with retry
def login():
    login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_btn = driver.find_element(By.ID, "submit-button")
    submit_btn.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))


# Function to book a class process that checks if the button text changed with retry
def book_class(booking_button):
    booking_button.click()
    # Wait for button state to change - will time out if booking failed
    wait.until(lambda d: booking_button.text == "Booked")

# Put the entire login flow into the retry-wrapper
retry(login, description="login")

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
booked_count = 0
waitlist_count = 0
already_booked_count = 0
processed_classes = []

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            class_info = f"{class_name} on {day_title}"

            if button.text == "Booked":
                print(f"✓ Already booked: {class_info}")
                already_booked_count += 1
                processed_classes.append(f"[Booked] {class_info}")
            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_info}")
                already_booked_count += 1
                processed_classes.append(f"[Waitlisted] {class_info}")
            elif button.text == "Book Class":
                # Use retry for entire booking action
                retry(lambda: book_class(button), description="Booking")
                print(f"✓ Successfully booked: {class_info}")
                booked_count += 1
                processed_classes.append(f"[New Booking] {class_info}")
                time.sleep(0.5)
            elif button.text == "Join Waitlist":
                # Use retry for entire waitlist action
                retry(lambda: book_class(button), description="Waitlisting")
                print(f"✓ Joined waitlist for: {class_info}")
                waitlist_count += 1
                processed_classes.append(f"[New Waitlist] {class_info}")
                time.sleep(0.5)

# ----------------  Verify Class Bookings on My Bookings Page ----------------

total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

# Function to navigate to my bookings with retry
def get_my_bookings():
    my_bookings_link = wait.until(ec.element_to_be_clickable((By.ID, "my-bookings-link")))
    my_bookings_link.click()
    # Wait for page to load - will time out if navigation failed
    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

    cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

    # Ensure we actually found cards - if empty, the page might not have loaded
    if not cards:
        raise TimeoutException("No booking cards found - page may not have loaded")
    return cards


# Put navigation to the Bookings page and get cards in the retry wrapper
all_cards = retry(get_my_bookings, description="Get my bookings")

verified_count = 0

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        # Skip if no "When:" text found (not a booking card)
        pass

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")

# Getting a SessionNotCreatedException?
# Remember to *Quit* Selenium's Chrome Instance before trying to click "run"

"""

