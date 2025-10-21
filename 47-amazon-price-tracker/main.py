from bs4 import BeautifulSoup
import requests
import os
import smtplib

MY_EMAIL = os.environ.get("DEV_EMAIL")
GMAIL_PASSWORD = os.environ.get("DEV_GMAIL_APP_PW")
BUY_PRICE = 100
endpoint = "https://appbrewery.github.io/instant_pot/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/140.0.0.0 Safari/537.36",
    "Accept-Language": "en-US",
    }


response = requests.get(endpoint, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

dollars = soup.find(name='span', class_='a-price-whole')
cents = soup.find(name='span', class_='a-price-fraction')
# product_name = soup.find(name='span', class_="a-size-large product-title-word-break").get_text().strip()
product_name = soup.find(id='productTitle').get_text().strip()
float_price = float(dollars.text + cents.text)

if float_price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=GMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Amazon Price Alert!\n\n"
                                f"{product_name}\n"
                                f"Current Price: ${float_price}\n"
                                f"{endpoint}"
                            )


# ----------------------------------------------- TESTING ----------------------------------------------- #
# endpoint = "https://appbrewery.github.io/instant_pot/"
#
# response = requests.get(endpoint)
# with open('website.html', 'w') as f:
#     f.write(response.text)


# total_price = soup.find(name='span', class_='a-offscreen')
# print(float_price)
# print(total_price.text)
# print(f"${dollars.text}{cents.text}")
# print(product_name)


