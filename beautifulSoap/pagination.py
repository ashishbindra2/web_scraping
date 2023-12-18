# pagination
from bs4 import BeautifulSoup
import requests

root = "https://subslikescript.com/"

website_url = root + 'movies?page=1'
response = requests.get(website_url)

try:
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
    exit()

html_content = response.text
soup = BeautifulSoup(html_content, 'lxml')
article = soup.find('article', class_='main-article')
pagination = soup.find('ul', class_='pagination')
pages = soup.find_all('li', class_='page-item')
last_page = pages[-2].text
for page in range(1,int(last_page)+1)[:10]:
    website_url = root + f'movies?page={page}'
    response = requests.get(website_url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')
    article = soup.find('article', class_='main-article')
    if article:
        anchor = article.find_all('a', href=True)
        links = []
        for link in anchor:
            website = root + link['href']
            response = requests.get(website)
            html_content = response.text
            soup = BeautifulSoup(html_content, 'lxml')
            articles = soup.find('article', class_='main-article')
            title = articles.find('h1').getText()
            valid_chars = "-_() ."
            title = ''.join(c if c.isalnum() or c in valid_chars else '_' for c in title)

            print(title)
            script = articles.find('div', class_="full-script").getText(separator=' ', strip=True)

            with open(f'output/pagination/{title}.txt', 'w', encoding='utf-8') as file:
                file.write(script)
    else:
        print("Article not found on the page.")
