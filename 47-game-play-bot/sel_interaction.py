from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

endpoint = "https://en.wikipedia.org/wiki/Main_Page"
endpoint_exercise = "https://secure-retreat-92358.herokuapp.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(endpoint_exercise)

# Clicking on a found element
# total_wiki_articles = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# total_wiki_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
# print(total_wiki_articles.text)
# total_wiki_articles.click()

# Find the element by text link and click the link
# all_portals = driver.find_element(By.LINK_TEXT, 'Content portals')
# all_portals.click()

# Sending keyboard input
# search_bar = driver.find_element(By.NAME, 'search')
# search_bar.send_keys("python", Keys.ENTER)

first_name = driver.find_element(By.NAME, 'fName')
last_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')

first_name.send_keys("First")
last_name.send_keys("Last")
email.send_keys("myemail@email.com")#, Keys.ENTER)

submit = driver.find_element(By.CSS_SELECTOR, 'form button')
submit.click()
# driver.quit()
