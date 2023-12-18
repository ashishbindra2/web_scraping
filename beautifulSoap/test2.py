# scraping into single page
from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/series/Friends-108778/season-1/episode-1-The_One_Where_Monica_Gets_a_Roommate'
response = requests.get(website)
content = response.text

soup = BeautifulSoup(content, 'lxml') # content, parser
# print(soup.prettify())
article = soup.find('article',class_='main-article')
title = article.find('h1').getText()
print(title)
print()
plot = article.find('p',class_='plot').getText()
print(plot)
script = article.find('div',class_="full-script").getText(strip=True, separator=' ')
print(script)