import requests 
from bs4 import BeautifulSoup


url = 'https://quotes.toscrape.com/'

response = requests.get(url)



# print(response)
# print(type(response.text))
print("\n=======================\n")

soup = BeautifulSoup(
    markup=response.text, 
    features = "html.parser"
)

# print(soup)
# print(type(soup))
print("\n=======================\n")

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tag_groups = soup.find_all('div', class_='tags')

# print(quotes)
# print(len(quotes))

for i in range(len(quotes)):
        print(quotes[i].text) 
        print(authors[i].text) 
        print("\n-----------------------\n")
        tags = tag_groups[i].find_all('a')
        for tag in tags: 
            print(tag.text) 
        print("\n=======================\n")