import requests 
import json

url = 'https://reqres.in/api/users/'
response = requests.get(url)

json_data = response.text

data = json.loads(json_data)
data_str = json.dumps(data, indent=4)

# print(type(data))
# print(type(data_str))
# print(data)
# print("==============================================")
print(data_str)