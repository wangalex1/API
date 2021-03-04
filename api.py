# Импортируем библиотеку requests
import requests
import json
# Адрес api метода для запроса get
url = 'https://api.oilpriceapi.com/v1/prices/latest'
headers = {
    'Authorization': 'Token ab263ccaf9869659d5021374960f4a69',
    'Content-Type': 'application/json'
}
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    print(text)
# Отправляем get request (запрос GET)
response = requests.get(url = url, headers = headers)

jprint(response.json())

with open('jprint.json', 'w') as f:
    json.dump(response.json(), f)