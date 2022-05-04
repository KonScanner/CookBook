import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes, authors = soup.find_all(
    'span', class_='text'), soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(len(quotes)):
    print(quotes[i].text, authors[i].text, sep='\n')
    quoteTags = tags[i].find_all('a', class_='tag')
    for qt in quoteTags:
        print(qt.text)
