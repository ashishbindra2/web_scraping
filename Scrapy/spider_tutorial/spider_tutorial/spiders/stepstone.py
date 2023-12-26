import scrapy


class StepstoneSpider(scrapy.Spider):
    name = "stepstone"
    allowed_domains = ["www.stepstone.be"]
    start_urls = ["https://www.stepstone.be"]

    def start_requests(self):
        yield scrapy.Request(url="https://www.stepstone.be", callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0'})

    def parse(self, response):
        pass


