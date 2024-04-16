STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
from twilio.rest import Client
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


account_sid = mystd
auth_token = mythoken
verified_number = myphone


STOCK_PRICE_API = "OMPBI9W91ZW27U9O"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_NAME,
    "datatype": "json"
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "521345dccf784eba9dfc0be84dd785da"


stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameter)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]
stock_list = [value for (key, value) in stock_data.items()]
yestaday_stock = stock_list[0]
yestaday_close = yestaday_stock["4. close"]
day_before_yestaday = stock_list[1]
day_before_yestaday_close = day_before_yestaday["4. close"]

result_stock = round(100 * (float(day_before_yestaday_close) - float(yestaday_close)) / float(yestaday_close))
up_down = None
if abs(result_stock) >= 5:
    if result_stock > 0:
        up_down = "⤴"
    else:
        up_down = "⤵"

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_parameter = {
        "apiKey": NEWS_API,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameter).json()
    articles = news_response["articles"]
    three_articles = articles[:3]
    formatted_article = [f"{STOCK_NAME}{result_stock}%{up_down}\nHeadline: {article["title"]}. \nBrief: {article["description"]}" for article in three_articles]


    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=formatted_article,
        from_=twiliophone,
        to=myphone
    )




## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

