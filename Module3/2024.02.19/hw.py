import requests

url = 'https://reqres.in/api/register'

payload = {
    'email': 'lindsay.ferguson@reqres.in',
    'password': 'qwerty12'
}

response = requests.get(url, data=payload)

print(response.request.body)