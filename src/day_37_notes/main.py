import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "kjskwnxi8b9w8i3o6",
    "username": "hudspeth199",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
