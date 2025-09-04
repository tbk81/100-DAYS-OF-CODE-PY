import os

import requests

STOCK_NAME = "RNA"
STOCK_NAME_TEST = "GOOGL"
COMPANY_NAME = "Google"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = os.environ.get("AV_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = os.environ.get("NEWS_API")

av_stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME_TEST,
    "apikey": STOCK_API
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API
}

stock_response = requests.get(STOCK_ENDPOINT, params=av_stock_params)
stock_data = stock_response.json()
print(stock_data)
daily_close = stock_data["Time Series (Daily)"]
daily_li = [value for (key, value) in daily_close.items()]
today_close = float(daily_li[0]["4. close"])
# print(f"{today_close}\n")
yesterday_close = float(daily_li[1]["4. close"])
# print(f"{yesterday_close}\n")
close_diff = abs(today_close - yesterday_close)
print(close_diff)
close_prices = (today_close, yesterday_close)
close_percentage = 1 - (min(close_prices) / max(close_prices))
print(close_percentage)

if close_percentage >= 0.05:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()
    article_li = news_data["articles"][:3]
    headlines = [f"Headline: {article_li[0]}" for article in article_li]
    print(news_data)
    print(article_li)


# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.



# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
or
TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
"""








