import scrapy


class WorldmeterSpider(scrapy.Spider):
    name = "worldmeter"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        # title = response.xpath("//div[@id='top20']/text()").get()
        # countries = response.xpath('//span[@class="t20-country"]/a/text()').getall()
        countries = response.xpath('//td/a')

        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # absolute_url = f'https://www.worldometers.info{link}'
            # absolute_url = response.urljoin(link)

            # yield scrapy.Request(url=absolute_url)
            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': country_name})
            # yield {
            #     'country_name': country_name,
            #     'link': link,
            # }

    def parse_country(self, response):
        rows = response.xpath('(//table[contains(@class,"table")])[1]/tbody/tr')
        country = response.request.meta['country_name']
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath('//td[2]/strong/text()').get()

            yield {
                'country': country,
                'year': year,
                'population': population,
            }
