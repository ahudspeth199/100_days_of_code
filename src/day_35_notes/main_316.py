import os

import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Enpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "bdbd1a38facdc607a632669c78513d3b"
account_sid = "ACe8821ff8d631d56524b27a015e71179f"
auth_token = ""

weather_params = {
    "lat": 33.804821,
    "lon": -84.172440,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

response = requests.get(OWM_Enpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token,http_client=proxy_client)
    message = client.messages \
        .create(
        body="Join Earth's mightest heros. L",
        from="+9393928",
        to="Your verified number"
    )
    print(message.status)
