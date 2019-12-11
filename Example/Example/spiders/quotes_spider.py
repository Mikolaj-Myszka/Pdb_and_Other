import scrapy
from ..items import ExampleItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        quote_item = ExampleItem()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('a.tag::text').extract()

            quote_item['title'] = title
            quote_item['author'] = author
            quote_item['tag'] = tag

            yield quote_item
