from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/series/Friends-108778/season-1/episode-1-The_One_Where_Monica_Gets_a_Roommate'
response = requests.get(website)
content = response.text

soup = BeautifulSoup(content, 'lxml') # content, parser
print(soup.prettify())
