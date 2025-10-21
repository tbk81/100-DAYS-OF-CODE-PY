from bs4 import BeautifulSoup
import requests

# endpoint = "https://appbrewery.github.io/instant_pot/"
#
# response = requests.get(endpoint)
# with open('website.html', 'w') as f:
#     f.write(response.text)

with open('website.html', 'r') as file:
    data = file.read()

soup = BeautifulSoup(data, 'html.parser')

# print(soup)
dollars = soup.find(name='span', class_='a-price-whole')
cents = soup.find(name='span', class_='a-price-fraction')
price = soup.find(name='span', class_='a-offscreen')
print(price.text)
print(f"${dollars.text}{cents.text}")



# ----------------------------------------------- TESTING ----------------------------------------------- #

