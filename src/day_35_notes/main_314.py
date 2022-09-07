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
print(weather_data)
