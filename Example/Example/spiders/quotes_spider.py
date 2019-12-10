import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        """ # Example 1
        title = response.css('title::text').extract()
        yield {'title_text': title}
        """
        """
        all_div_quotes = response.css('div.quote')
        title = all_div_quotes.css('span.text::text').extract()
        author = all_div_quotes.css('.author::text').extract()
        tag = all_div_quotes.css('a.tag::text').extract()
        yield {
            'title': title,
            'author': author,
            'tag': tag
        }
        """
        # Example of getting data one by one
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('a.tag::text').extract()
            yield {
                'title': title,
                'author': author,
                'tag': tag
            }
