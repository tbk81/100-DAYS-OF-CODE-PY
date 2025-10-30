import os
import requests
from bs4 import BeautifulSoup



GOOGLE_FORM = os.environ.get("GOOGLE_FORM_D53")

zillow_endpoint = "https://appbrewery.github.io/Zillow-Clone/"

def write_site(site):
    response = requests.get(site)
    with open('website.html', 'w') as file:
        file.write(response.text)


# write_site(zillow_endpoint)

with open('website.html') as f:
    data = f.read()
soup = BeautifulSoup(data, 'html.parser')

addresses = soup.find_all(name='address')
for addr in addresses:
    print(addr.text.strip().replace("| ", ",").split(",")[1:])

