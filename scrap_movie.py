import requests
from bs4 import BeautifulSoup

website_data = requests.get('https://subslikescript.com/movies_letter-M')
content = website_data.text


movies = BeautifulSoup(content,'lxml')

article = movies.find('article',class_='main-article')
heading = article.find('h1').getText()
print(heading)
#movies_names = article.find_all('a', href=True)

#for link in movies_names:
#	print(link.getText())