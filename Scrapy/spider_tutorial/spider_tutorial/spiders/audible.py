from typing import Iterable

import scrapy
from scrapy import Request


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.in"]
    start_urls = ["https://www.audible.in/search"]

    def start_requests(self):
        yield scrapy.Request(url="https://www.audible.in/search", callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0'})

    def parse(self, response):
        product_container = response.xpath('//div[@class="adbl-impression-container "]/div/span[2]/ul/li')

        for product in product_container:
            # book_author = product.xpath('//li[@class="bc-list-item"]/h3/a/text()').getall()
            book_title = product.xpath('.//h3[contains(@class, "bc-heading")]/a/text()').get()
            book_author = product.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').getall()
            book_length = product.xpath('.//li[contains(@class, "runtimeLabel")]/span/text()').get()

            yield {
                'title': book_title,
                'author': book_author,
                'length': book_length,
                'User-Agent': response.request.headers['User-Agent']
            }

            pagination = response.xpath('//ul[contains(@class,"pagingElements")]')
            next_page_url = pagination.xpath('.//span[contains(@class,"nextButton")]/a/@href').get()

            if next_page_url:
                yield response.follow(url=next_page_url, callback=self.parse, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0'})
