import requests 
from bs4 import BeautifulSoup

def getHTML(url: str):
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"Something went wrong. Error: {e}")
        return None

url = "https://kolesa.kz/cars/"
html = getHTML(url)

if html:
    bs = BeautifulSoup(html, 'html.parser')
    pager = int(bs.find('div', 'row pager-row').find_all('a')[-2].text)
    
    all_prices = bs.find('span', class_ = 'a-card__price')
    
    for price in all_prices:
        print(price.text.replace(" ", ""))
else:
    print('Something is wrong!')

pager = bs.find('div', 'row pager-row')
