import requests
import csv
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

response = requests.get(url)

soup = BeautifulSoup(
    markup=response.text, 
    features = "html.parser"
)

# info = soup.find_all('div', class_='p-4')
titles = soup.find_all('h4')
prices = soup.find_all('h5')

file_path = "2024.02.14/data.csv"

with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(["Data:"])
    
    for title, price in zip(titles, prices):
        writer.writerow([title.text, price.text])
        writer.writerow(["======================="])
    
