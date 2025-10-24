from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time

# Set up web driver
endpoint = 'https://ozh.github.io/cookieclicker/'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(endpoint)

# Wait to page to load before clicking
sleep(2)

print("Looking for language selector and consent button")
try:
    lang_select = driver.find_element(By.ID, 'langSelect-EN')
    lang_select.click()

    sleep(2)
    consent_banner = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
    consent_banner.click()
except NoSuchElementException:
    print("Language selection or consent banner not found")

sleep(1)
cookie = driver.find_element(By.ID, 'bigCookie')
for n in range(20):
    cookie.click()

# side_note = driver.find_element(By.XPATH, '//*[@id="notes"]/div[5]')
# side_note.click()


products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
# products[0].click()
best_item = None
for product in reversed(products):  # Start from most expensive (bottom of list)
    # Check if item is available and affordable (enabled class)
    if "enabled" in product.get_attribute("class"):
        best_item = product
        break

# Buy the best item if found
if best_item:
    best_item.click()


