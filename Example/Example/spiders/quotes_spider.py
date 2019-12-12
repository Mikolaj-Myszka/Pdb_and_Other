import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import ExampleItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # page_number = 2
    start_urls = [
        # 'http://quotes.toscrape.com/'
        # 'http://quotes.toscrape.com/page/1/'
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        # print('token: ', token)
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'costam',
            'password': 'trolololo'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
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
