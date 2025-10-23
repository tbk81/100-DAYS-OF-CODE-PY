from selenium import webdriver
from selenium.webdriver.common.by import By

endpoint = ("https://www.amazon.com/GIGABYTE-Graphics-WINDFORCE-GV-N507TEAGLE-OC-16GD/dp/B0DTR7GWG6/"
             "ref=sr_1_4?crid=YN5MPXH4A07C&dib=eyJ2IjoiMSJ9.oxR3lxS23wOOzZKi3U31b6tuf2zmnBnIaWS3VhBr6Qq6yyUNkrbDt9"
             "-PrI6CW-dOg4JNs7mVGmWbqujk_gLHTa-QMJ_Okoqvh9uvdB-O2R9lD4giqWPuds1SK9HtXEN1YLY7btDPFg2S"
             "_QemDUvUzaW1lfGtr89QNT2viwJDzOghudhSbALaI_hAA0A_v6CfJKqdBlxT8DfaYNbcfKpiLhMxW20qomFcujY3vJoqWlY"
             ".JAtH5EJc2Gr2vz-aIWX6qMbJORy7SChHNEzS7raSsjo&dib_tag=se&keywords=gtx%2B5070%2Bti&qid=1761177738&sprefix"
             "=gtx%2B5070%2Caps%2C157&sr=8-4&th=1")

python_org = "https://www.python.org"

# Keep chrome open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(python_org)

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# print(f"price = {price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


driver.quit()



# ----------------------------------------------- TESTING ----------------------------------------------- #
# driver.close()  # closes the particular tab
# driver.quit()  # shuts down the entire browser



