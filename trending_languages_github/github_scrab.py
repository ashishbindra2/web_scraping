import time
import requests
from bs4 import BeautifulSoup

base_url = "https://github.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36 Edg/135.0.0.0'
}

def github_treading_language(url = "https://github.com/trending/python"):

    html_doc = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    box = soup.find('div', class_='Box')

    articles = box.find_all('article')

    language = ''
    trends = []
    for article in articles:
        heading = article.find('h2')
        description_p = article.find("p")
        description = ''
        
        if description_p:
            description = description_p.get_text(strip=True)
        
        repo_link = heading.find('a', href=True,)
        trends.append(repo_link['href'])
        
        data = article.find('span', itemprop='programmingLanguage')
        if data:
            language = data.text
        # div = article.find('div', class_="f6 color-fg-muted mt-2")
        
        # links = div.find_all('a')
        
        # for i, link in enumerate(links,start=1):
        #     if i > 2:
        #         break
        #     data = link.get_text(strip=True)
        #     print(data)

    for trend in trends:
        tags = []
        
        response = requests.get(base_url + str(trend), headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        detail_container = soup.find(id="repository-details-container")
        fork = detail_container.find("span", id="repo-network-counter").get('title', 'No title attribute')
        star = detail_container.find("span", id="repo-stars-counter-star").get('title', 'No title attribute')
        
        grids = soup.find_all("div",class_="BorderGrid-row")
        lis = grids[-1].find_all('li')
        
        languages = {}
        for li in lis:
            spans = li.find_all('span')
            lang = spans[0].get_text(strip=True)
            per = spans[1].get_text(strip=True)
            
            if lang:
                languages[lang] = per
            
        about = soup.find('div',class_ = "BorderGrid-cell")
        tag = about.find('div', class_ = "f6")
        description_p = about.find('p')
        
        description = ''
        if description_p:
            description = description_p.get_text(strip=True)
        
        if tag:
            links = tag.find_all('a')
            for link in links:
                tags.append(link.get_text(strip=True)) 
        time.sleep(1)        
        
        yield{
            "id": str(trend), 
            "description": description, 
            "stars": star, 
            "forks": fork, 
            "tags": tags,
            "language": language,
            "languages":languages
            }



def edges_extraction(tags:list, temp_tags:list):
    new_tag = []
    for tag in tags:
        if tag in temp_tags:
            new_tag.append(tag)
    return new_tag