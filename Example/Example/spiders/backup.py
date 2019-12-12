import scrapy
from ..items import ExampleItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        # 'http://quotes.toscrape.com/'
        'http://quotes.toscrape.com/page/1/'
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

        """
        next_page = response.css('li.next a::attr(href)').get()
        print(next_page)

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        """

        next_page = 'http://quotes.toscrape.com/page/' + str(self.page_number) + '/'

        if self.page_number < 11:
            self.page_number += 1
            yield response.follow(next_page, callback=self.parse)
