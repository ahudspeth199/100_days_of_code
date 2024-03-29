import requests
from datetime import datetime

USERNAME = "hudspeth199"
TOKEN = "kjskwnxi8b9w8i3o6"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y*m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}

response = requests.post(url=pixel_creation_endpoint,json=pixel_data, headers=headers)
print(response.text)
