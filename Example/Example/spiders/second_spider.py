import scrapy
from Example.items import ExampleItem


class SecondSpider(scrapy.Spider):
    name = 'secondspider'
    allowed_domains = ['www.superdatasciencecom']
    start_url = ['https://www.superdatascience.com/']

    def parse(self, response):
        item = ExampleItem()
        #item['main_headline'] = response.xpath('//span/text()').extract()
        item['headline'] = response.xpath('//title/text()').extract()
        item['spider'] = self.name

        return item





