
### Scrapy ###

---
To installing using conda <br>
`conda install -c conda-forge scrapy`
---
Install in ubuntu <br>
`sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev`
---
virtual venv<br>
`pip install scrapy`

#### Scrapy there are two popular templates
1. Scrapy.spider
2. CrawlSpider
---
1. scrapy.spyder
---------------
it is the simplest spider 
it doesn't provide any special functionality,but we can customize this template scrape the way we want 

2. Crawl.spyder
---------------
- Crawl spyder is the most commonly used spyder for crawling regular website 
- It provides some mechanisms, for following links by defining a set of rules.
> Note that Crawling is not the same as scraping a website

___
A crawler usually browses the world wide web for purpose of web indexing.
But web scraping is more about extracting information from websites.
____
In scrapy we used `resonse` to find elements
it is just like driver in selenium or soup in beautiful soup
> unlike selenium, we can only find elements with XPath on scrapy

Finding Elements with Scrapy
---
`response.xpath('//tag[@AttributeName=Value"]')`

`response.xpath().get()`
`response.xpath().getall()`

demo program
---

` scrapy bench`
`scrapy fetch http://google.com `
`scrapy startproject spider_tutorial`
`cd spider_tutorial`
`scrapy genspider worldmeter www.worldometers.info/world-population   
scrapy shell`
> r = scrapy.Request(url = "https://www.worldometers.info/world-population/") 
> fetch(r) 
> response.body
> response.xpath("//div[@id='top20']")                                        
> response.xpath("//div[@id='top20']").get()
> response.xpath("//div[@id='top20']/text()").get() 
> response.xpath("//div[@class='t20-line']").getall()        
> response.xpath('//span[@class="t20-country"]/a/text()').getall()
`

To run a scrapy file
`scrapy crawl filename`

three diffenet way to work with url`
Relative link: 
 `scrapy.Request(url=link)`

`response.urljoin(link)`
we don't have to concatenate url urljoin tak care of it

relative url
`response.follow(url)`

callback argument 
---
it calls every time when it got a new link

Meta Argument
---
`meta={'country_name': country_name}
country = response.request.meta['country_name']`


save data in json
---
`scrapy crawl filename - jsonfile.json`

create a project 
---
scrapy genspider project_name website_link 