import requests 
import csv
from bs4 import BeautifulSoup

url_pattern = 'https://ru.euronews.com/'
file_path = 'news_data.csv'

def get_data(page_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    
    response = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
        
    titles = soup.find_all('div', class_='m-object__metas')
    links = soup.find_all('a', class_='m-object__title__link')
    descriptions = soup.find_all('h2', class_='m-object__title qa-article-title')
    

    data = []
    for title, link, description in zip(titles, links, descriptions):
        title_text = title.text.strip()
        link_url = link.get('href')
        description_text = description.text.strip() if description else ''
        data.append([title_text, link_url, description_text])
    
    print("Titles found:", len(titles))
    print("Links found:", len(links))
    print("Descriptions found:", len(descriptions))

    return data

def scrape_and_write_csv(url_pattern, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Links', 'Description'])
        
        
        page_url = url_pattern.format()
        page_data = get_data(page_url)
           
        for row in page_data:
            writer.writerow(row)

scrape_and_write_csv(url_pattern, file_path)

