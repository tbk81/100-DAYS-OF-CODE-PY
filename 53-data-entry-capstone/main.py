import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


GOOGLE_FORM = os.environ.get("GOOGLE_FORM_D53")
zillow_endpoint = "https://appbrewery.github.io/Zillow-Clone/"

# Chrome and driver setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)



def write_site(site):
    response = requests.get(site)
    with open('website.html', 'w') as file:
        file.write(response.text)


# write_site(zillow_endpoint)

with open('website.html') as f:
    data = f.read()
soup = BeautifulSoup(data, 'html.parser')

# Find and list addresses
addresses = soup.find_all(name='address')
addr_li = [addr.get_text().replace(" | ", " ").strip() for addr in addresses]

# Find and list prices
prices = soup.select(".StyledPropertyCardDataWrapper span")
price_li = [price.get_text().replace("/mo", "").split("+")[0] for price in prices]

# Find and link all links
links = soup.select(".StyledPropertyCardDataWrapper a")
link_li = [link['href'] for link in links]

# Log into website
driver = webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_FORM)

# Log into website
wait = WebDriverWait(driver, 2)

# address_input = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']")))
# address_input.send_keys(addr_li[0])
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']")))
form_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
# form_inputs[0].send_keys(addr_li[0])

submit_button = driver.find_element(By.CSS_SELECTOR, "div[role='button']")
# submit_button.click()

# for i in range(len(form_inputs)):
#     form_inputs[i].send_keys(addr_li[0])
#     form_inputs[i].send_keys(price_li[0])
#     form_inputs[i].send_keys(link_li[0])

form_inputs[0].send_keys(addr_li[0])
form_inputs[1].send_keys(price_li[0])
form_inputs[2].send_keys(link_li[0])
submit_button.click()
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "a[href=https]")))
another_response = driver.find_element(By.CSS_SELECTOR, "a[href=https]")
another_response.click()


# ==================================== TESTING AND DEV ==================================== #

# addresses = soup.select(".StyledPropertyCardDataWrapper address")
# for addr in addresses:
    # print(addr.text.strip())
    # print(addr.get_text().strip().replace("| ", ",").split(",")[1:])
    # print(addr.get_text().replace(" | ", " ").strip())
# li = [addr.get_text().strip().replace("| ", ",").split(",")[1:] for addr in addresses]


# <input type="text" class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="off"
# tabindex="0" aria-labelledby="i6 i9" aria-describedby="i7 i8" aria-disabled="false"
# dir="auto" data-initial-dir="auto" data-initial-value="">

# <input type="text" class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="off"
# tabindex="0" aria-labelledby="i1 i4" aria-describedby="i2 i3" aria-disabled="false"
# dir="auto" data-initial-dir="auto" data-initial-value="747 Geary Street, 747 Geary St, Oakland, CA 94609" badinput="false">


"""
Types of CSS Selectors with Examples:

ID Selector (#) – Selects a single, unique element by its id.
Class Selector (.) – Selects one or multiple elements sharing the same class.
Attribute Selector – Targets attributes like href, name, placeholder, etc.
Combining Attributes – Useful when a single attribute is not unique.
Substring Matching – Allows partial string matching:

Prefix (^) – starts with
Suffix ($) – ends with
Contains (*) – substring

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#open Chrome
driver = webdriver.Chrome()
#navigate to the site
driver.get("https://quotes.toscrape.com")
#find the h1 element
h1 = driver.find_element(By.CSS_SELECTOR, "h1")
#print the h1 element
print(f"H1 element: {h1.text}")
#find all quotes (span elements with the class: 'text')
quotes = driver.find_elements(By.CSS_SELECTOR, "span[class='text']")
for quote in quotes:
    print(f"Quote: {quote.text}")
#find all tags (anything with the class 'tag')
tags = driver.find_elements(By.CSS_SELECTOR, ".tag")
for tag in tags:
    print(f"Tag: {tag.text}")
#find the login link (first a element with href: '/login')
login_link = driver.find_element(By.CSS_SELECTOR, "a[href='/login']")
login_link.click()
#find the username box (element with ID: 'username')
username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("some text")
#find the password box (input elements with the type: 'password')
password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
password.send_keys("my super secret password")
#sleep 5 seconds so the user can see the filled input boxes
sleep(5)
driver.quit()

"""

