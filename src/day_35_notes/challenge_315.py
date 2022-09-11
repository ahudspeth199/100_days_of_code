# Objective: print "Bring an Umbrella" if any of the next 12 hourly weather condition codes is less than 700.

#HINT
'''
1. Practice printing out the weather ID for the weather in the 0th hour.
2. Try to create a slice from the weather data to get a list of the hourly forecasts for only the next 12 hours.
3. Using the above try to create a list of only the next 12 weather condition codes.
'''
import requests

OWM_Enpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "bdbd1a38facdc607a632669c78513d3b"

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
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        print("Bring an umbrella.")


#print(weather_data["hourly"][0]["weather"][0]["id"])
