import requests
import json

url = 'https://reqres.in/api/register'

payload = {
    'email': 'lindsay.ferguson@reqres.in',
    'password': 'qwerty12.3434'
}

response = requests.post(url, data=payload)
# response = requests.post(url, data=json.dumps(payload))
# response = requests.post(url, params=payload)

json_data = response.text


data = json.loads(json_data)

data_str = json.dumps(data, indent=4)
print(data_str)
print("================================================")
print(response.url)
print(response.request.headers)
print(response.request.body)
