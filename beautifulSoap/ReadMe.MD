BeautifulSoup
---
- Download and execute Microsoft C++ Build Tools to install the Visual Studio Installer.
- it is the easiest python library for web scraping.
- it has some dependencies,such as need of the request libray to make requests.
- can pull data from email and XML files
- it uses  of external parcels to track data like XML and HTML parser
- it is not first choice for large web scraping projects to scrape websites because of dependencies 

>to test scraping: https://subslikescript.com/

---
To installing using conda <br>
`conda install -c conda-forge scrapy`
---
Install in ubuntu <br>
`sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev`
---
virtual venv<br>
`pip install scrapy`
---

libraries :<br>
`from bas4 import Beautiful Soup`<br>
`import requests`

Steps before scraping a website
-------------------------------
1. Fetch the pages(obtained a response object)<br>
    `result = rquests.get('www.google.com')'`
2. Page content<br>
    `content = result.text`
3. create soup<br>
    `soup = BeautifulSoup(content,'lxml')'`
4. to locate id<br>
    `soup.find(id="specific_id")`
5. to locate element by name<br>
    `soup.find('tag',class_="class_name")`
6. locate element using tag name<br>
    `soup.find('h1)` --> return only an element
7. Find  elements(multiple element) using tag name<br>
    `soup.find_all('h2')` --> it return list

It's recommended to find elements in this order.
1. ID
2. Class Name
3. Rag Name, CSS Selector
4. XPATH
