import requests
from datetime import datetime

TOKEN = mytoken
USERNAME = myname
GRAPHID = "graph1"

pixela_end = "https://pixe.la/v1/users"
user_parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create_response = requests.post(url=pixela_end,json=user_parameter)
# print(create_response.text)

graph_end = f"{pixela_end}/{USERNAME}/graphs"
graph_parameter = {
    "id": "graph1",
    "name": "walk",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_end, json=graph_parameter, headers=headers)
# print(response.text)

today = datetime.now()

score_end = f"{pixela_end}/{USERNAME}/graphs/{GRAPHID}"
score_parameter = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.12",
}

response = requests.post(url=score_end, json=score_parameter, headers=headers)
print(response.text)

update_end = f"{pixela_end}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
update_params = {
    "quantity": "4.34"
}

# response = requests.put(url=update_end, json=update_params, headers=headers)
# print(response.text)


#delete_end = f"{pixela_end}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
#response = requests.delete(url=delete_end, headers=headers)
print(response.text)
