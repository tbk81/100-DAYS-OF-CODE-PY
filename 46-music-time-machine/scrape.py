import requests
from bs4 import BeautifulSoup

endpoint = "https://www.billboard.com/charts/hot-100/2000-08-26"

response = requests.get(endpoint)
print(response.text)


