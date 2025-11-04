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

# Find and list addresses
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

address_input = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']")))
address_input.send_keys(addr_li[0])

# price_input = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "whsOnd zHQkBf")))
# pw_input.send_keys(price_li[0])
#
# link_input = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "whsOnd.zHQkBf")))
# pw_input.send_keys(link_li[0])

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

