# If the ISS is close to my current position
# and it's currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60s

import requests
import datetime as dt
import random

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = dt.now()

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
    with open(sunrise, sunset) as quotes:
        lines = quotes.read().splitlines()
        q_message = random.choice(lines)

    import smtplib, ssl
