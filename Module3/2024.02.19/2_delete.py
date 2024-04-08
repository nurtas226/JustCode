import requests
import json

url = 'https://reqres.in/api/users/15'

# "DELETE"
response = requests.delete(url)


print(response)
print(response.url)