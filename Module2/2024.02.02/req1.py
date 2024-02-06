import requests

url = 'https://httpbin.org/image/jpeg'
response = requests.get(url)

with open('data/test.jpeg', 'wb') as f:
    f.write(response.content)