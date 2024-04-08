import requests 
from bs4 import BeautifulSoup


url = 'https://quotes.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(
    markup=response.text, 
    features = "html.parser"
)

####################################################

full_quotes = soup.find_all('div', class_='quote')

for full_quote in full_quotes:
    quote = full_quote.find('span', class_='text')
    author = full_quote.find('small', class_='author')
    tags = full_quote.find_all('a', class_='tag') 
    
    print(quote.text)
    print(author.text)
    
    tag_texts = [tag.text for tag in tags]
    print(", ".join(tag_texts)) 
    print("\n=======================\n")


# quotes = soup.find_all('span', class_='text')
# authors = soup.find_all('small', class_='author')
# tag_groups = soup.find_all('div', class_='tags')


# for i in range(len(quotes)):
#         print(quotes[i].text) 
#         print(authors[i].text) 
        
#         tags = tag_groups[i].find_all('a')
        
#         tag_texts = [tag.text for tag in tags]
#         print(", ".join(tag_texts)) 
#         print("\n=======================\n")