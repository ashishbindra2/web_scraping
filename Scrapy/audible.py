import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.in"]
    start_urls = ["https://www.audible.in/search"]

    def parse(self, response):
        product_container = response.xpath('//li[@class="bc-list-item productListItem"]')
        for product in product_container:
            