# Export data to a txt file
from bs4 import BeautifulSoup
import requests

# URL of the website to scrape
website_url = 'https://subslikescript.com/series/Friends-108778/season-1/episode-1-The_One_Where_Monica_Gets_a_Roommate'

# Make the HTTP request to the website
response = requests.get(website_url)

# Check if the request was successful
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
    # Handle the error or exit the script
    exit()

# Get the HTML content of the response
html_content = response.text

# Create a BeautifulSoup object with lxml parser
soup = BeautifulSoup(html_content, 'lxml')

# Find the main article section on the page
article = soup.find('article', class_='main-article')

# Check if the article section is found
if article:
    # Extract title from the h1 tag inside the article
    title = article.find('h1').getText()
    print(title)
    # Extract plot from the p tag with class 'plot' inside the article
    plot = article.find('p', class_='plot').getText()
    print(plot)

    # Extract script from the div tag with class 'full-script' inside the article
    script = article.find('div', class_="full-script").getText(separator=' ', strip=True)
    # Uncomment the line below if you want to print the script to the console
    # print(script)

    # Write the script to a file with UTF-8 encoding
    with open(f'{title[:7]}.txt', 'w', encoding='utf-8') as file:
        file.write(script)
else:
    print("Article not found on the page.")
