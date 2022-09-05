import requests

# My challenge to you is to make an API request from PyCharm to the one call API and to locate the hourly forecasts
# for the next 48 hours in the JSON response that you get back.

# Get your latitude and longitude from latlong.net
# Make a request to the One Call API using the request module
# Print out the HTTP status code that you get back
# Print the response to the console
# Copy-paste the response to the online json viewr
# locate the hourly forcast for the next 48 hours

# My Solution
'''
response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?lat=33.804821&lon=-84.172440&appid=bdbd1a38facdc607a632669c78513d3b")

print(response.json())
'''



OWM_Enpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "bdbd1a38facdc607a632669c78513d3b"

weather_params = {
    "lat": 33.804821,
    "lon": -84.172440,
    "appid": api_key,
}

response = requests.get(OWM_Enpoint, params=weather_params)
print(response.json())

