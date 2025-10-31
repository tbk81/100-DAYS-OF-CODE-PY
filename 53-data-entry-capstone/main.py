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

# Find and list addresses
# addresses = soup.find_all(name='address')
# addr_li = [addr.get_text().replace(" | ", " ").strip() for addr in addresses]

# Find and list addresses
# prices = soup.select(".StyledPropertyCardDataWrapper span")
# price_li = [price.get_text().replace("/mo", "").split("+")[0] for price in prices]

# Find and link all links
links = soup.select(".StyledPropertyCardDataWrapper a")
link_li = [link['href'] for link in links]
print(link_li)



# ==================================== TESTING AND DEV ==================================== #

# addresses = soup.select(".StyledPropertyCardDataWrapper address")
# for addr in addresses:
    # print(addr.text.strip())
    # print(addr.get_text().strip().replace("| ", ",").split(",")[1:])
    # print(addr.get_text().replace(" | ", " ").strip())
# li = [addr.get_text().strip().replace("| ", ",").split(",")[1:] for addr in addresses]


