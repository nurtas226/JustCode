import requests 
import csv
from bs4 import BeautifulSoup

url_pattern = 'https://www.nike.com/pl/w/mezczyzni-buty-nik1zy7ok'
file_path = 'nike_shoes_data.csv'

def get_data(page_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    
    response = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
        
    prices = soup.find_all('div', class_='product-price pl__styling is--current-price css-11s12ax')
    names = soup.find_all('div', class_='product-card__title')
    colors = soup.find_all('div', class_='product-card__count-item')
    links = soup.find_all('a', class_='product-card__link-overlay')
    

    data = []
    for price, name, color, link  in zip(prices, names, colors, links):
        price_text = price.text.strip()
        name_text = name.text.strip()
        color_text = color.text.strip()
        link_url = link.get('href')
        data.append([price_text, name_text, color_text, link_url])

    return data

def scrape_and_write_csv(url_pattern, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price', 'Name', 'Colors', 'Link'])
        
        page_url = url_pattern.format()
        page_data = get_data(page_url)
           
        for row in page_data:
            writer.writerow(row)

scrape_and_write_csv(url_pattern, file_path)