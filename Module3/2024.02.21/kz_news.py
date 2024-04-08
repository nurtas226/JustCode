import requests 
import csv
from bs4 import BeautifulSoup

url_pattern = 'https://tengrinews.kz/'
num_pages = 1
file_path = 'news_data.csv'

def scrape_page(url):
    headers = {'FireFox': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    titles = soup.find_all('main-news_super_item_title')
    date = soup.find_all('main-news_super_item_meta')
    
    data = []
    for title, price in zip(titles, date):
        data.append([title.text.strip(), price.text.strip()])
    
    return data

def scrape_and_write_csv(url_pattern, num_pages, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Date'])
        
        for page_num in range(1, num_pages + 1):
            page_url = url_pattern.format(page_num)
            page_data = scrape_page(page_url)
           
            for row in page_data:
                writer.writerow(row)
                


scrape_and_write_csv(url_pattern, num_pages, file_path)
