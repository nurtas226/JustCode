import requests 
from bs4 import BeautifulSoup

def getHTML(url : str):
    try:
        response = requests.get(url=url)
        return response.text
    except Exception as e:
        print(f"Что-то пошло не так когда обращаюсь к {url}, Ошибка гласит : {e}")
        return None

def getPrice(soup : BeautifulSoup):
    prices = []
    all_divs = soup.find_all('span', 'a-card__price')
    for div in all_divs:
        prices.append(div.text)
    return prices

url = 'https://kolesa.kz/cars/toyota/camry/kostanai/'

html = getHTML(url)

if html:
    bs = BeautifulSoup(html, 'html.parser')
    pager = int(bs.find('div', 'row pager-row').find_all('a')[-2].text)
    prices = getPrice(bs)
    for page in range(2, pager + 1):
        link = url + f'?page={page}'
        html = getHTML(url=link)
        bs = BeautifulSoup(html, 'html.parser')
        for price in  getPrice(bs):
            prices.append(price)
else:
    print('Что-то не так!')
