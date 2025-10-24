from selenium import webdriver
from selenium.webdriver.common.by import By

endpoint = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(endpoint)

# total_wiki_articles = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
total_wiki_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
print(total_wiki_articles.text)


driver.quit()
