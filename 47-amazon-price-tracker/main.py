from bs4 import BeautifulSoup
import requests
import os
import smtplib

MY_EMAIL = os.environ.get("DEV_EMAIL")
GMAIL_PASSWORD = os.environ.get("DEV_GMAIL_APP_PW")
BUY_PRICE = 800
endpoint = "https://appbrewery.github.io/instant_pot/"
endpoint2 = ("https://www.amazon.com/GIGABYTE-Graphics-WINDFORCE-GV-N507TEAGLE-OC-16GD/dp/B0DTR7GWG6/"
             "ref=sr_1_4?crid=YN5MPXH4A07C&dib=eyJ2IjoiMSJ9.oxR3lxS23wOOzZKi3U31b6tuf2zmnBnIaWS3VhBr6Qq6yyUNkrbDt9"
             "-PrI6CW-dOg4JNs7mVGmWbqujk_gLHTa-QMJ_Okoqvh9uvdB-O2R9lD4giqWPuds1SK9HtXEN1YLY7btDPFg2S"
             "_QemDUvUzaW1lfGtr89QNT2viwJDzOghudhSbALaI_hAA0A_v6CfJKqdBlxT8DfaYNbcfKpiLhMxW20qomFcujY3vJoqWlY"
             ".JAtH5EJc2Gr2vz-aIWX6qMbJORy7SChHNEzS7raSsjo&dib_tag=se&keywords=gtx%2B5070%2Bti&qid=1761177738&sprefix"
             "=gtx%2B5070%2Caps%2C157&sr=8-4&th=1")
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/140.0.0.0 Safari/537.36",
    "Accept-Language": "en-US",
    }


response = requests.get(endpoint2, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

product_name = soup.find(id='productTitle').get_text().strip()
dollars = soup.find(name='span', class_='a-price-whole')
int_price = int(dollars.text.strip("."))
print(f"{product_name}\n{int_price}")


if int_price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=GMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Amazon Price Alert!\n\n"
                                f"{product_name}\n"
                                f"Current Price: ${int_price}\n"
                                f"{endpoint2}"
                            )


# ----------------------------------------------- TESTING ----------------------------------------------- #
# endpoint = "https://appbrewery.github.io/instant_pot/"
#
# response = requests.get(endpoint)
# with open('website.html', 'w') as f:
#     f.write(response.text)

# cents = soup.find(name='span', class_='a-price-fraction')
# product_name = soup.find(name='span', class_="a-size-large product-title-word-break").get_text().strip()

# total_price = soup.find(name='span', class_='a-offscreen')
# print(float_price)
# print(total_price.text)
# print(f"${dollars.text}{cents.text}")
# print(product_name)


