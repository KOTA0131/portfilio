import requests
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = mysid
auth_token = mytoken

verified_number = myphone



city = "Tokyo,Japan"
api_key = key
lat = 35.689487
lon = 139.691711
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_parameter = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(OWN_ENDPOINT, params=weather_parameter)
response.raise_for_status()
weather_data = response.json()
weather = weather_data["list"]
des = []
bring = []
for i in weather:
    des.append(i["weather"][0]["description"])
    y = i["weather"][0]["id"]
    if y < 700:
        bring.append(True)
    else:
        bring.append(False)

if bring:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_=twiliophone,
        to=myphone
    )
