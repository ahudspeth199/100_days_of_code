#This is the normal mode
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = "c0364269bac14629bcb5e1cd0ef8e756"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "4D69MWXCW85KCWS4"

TWILIO_SID ="ACe8821ff8d631d56524b27a015e71179f"
TWILIO_AUTH_TOKEN = "68ee03fff01ff4233003668255b0ecb1"

stock_param = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY,
    }

response = requests.get(STOCK_ENDPOINT, params=stock_param)
data = response.json()["Time Series (Daily)"]
#print(data)
##list data
#data_list = [new_item for item in list]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
#print(data_list)
print(yesterday_closing_price)


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)


differnce = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(differnce)


diff_percent = (differnce/ float(yesterday_closing_price)) * 100
print(diff_percent)


if diff_percent > 5:
  print("Get News")

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if diff_percent > 1:
    news_parms = {
        "apiKey": NEWS_API_KEY,
        "qinTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, news_parms)
    articles = news_response.json()['articles']
    print(articles)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
# Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]
print(three_articles)


# STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
#"Headline: {article titel}. \nBrief: {article description}"
#[new_item for item in list]
#[for article in three_articles]
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
#TODO 9. - Send each article as a separate message via Twilio.

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="+18585859702",
        to="My Phon number"
    )

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

