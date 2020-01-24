import scrapy
from scrapy.loader.processors import TakeFirst
from komputronik_products.itemloaders import KomputronikItemLoader
from komputronik_products.items import KomputronikProductsItem


class KomputronikProductSpider(scrapy.Spider):
    name = 'komputronik_product'
    start_urls = [
        # 'https://www.komputronik.pl/category/5022/laptopy.html?pr10%5B%5D=0\
        #     &pr10%5B%5D=1700&prod%5B%5D=23&filter=1&showBuyActiveOnly=0\
        #     &sort=1&by=f_price_10&showProducts=1',
        'https://www.komputronik.pl/category/5022/laptopy.html?pr10%5B%5D=0\
            &pr10%5B%5D=1400&prod%5B%5D=23&filter=1&showBuyActiveOnly=0\
            &sort=1&by=f_price_10&showProducts=1'
    ]
    page_number = 1
    last_page = 0

    def parse(self, response):
        if self.page_number == 1:
            self.last_page = int(
                response.css('div.pagination ul li a::text')[-1].extract()
            )

        # follow links to product pages
        page_links = response.xpath(
            '//div[@class="pe2-head"]//a/@href'
        ).extract()
        for url in page_links:
            yield response.follow(url, self.parse_product)

        # follow pagination links
        if self.page_number < self.last_page:
            self.page_number += 1
            next_page = self.start_urls[0] + '&p=' + str(self.page_number)
            yield response.follow(next_page, self.parse)

    def parse_product(self, response):
        item_loader = KomputronikItemLoader(
            item=KomputronikProductsItem(), response=response
        )
        item_loader.add_xpath('name', '//h1/text()')
        item_loader.add_xpath(
            'price', '//span[@class="proper"]/text()', TakeFirst()
        )
        item_loader.add_xpath(
            'availability', '//a[@class="tooltip-wrap pretty"]/text()',
            re='Wysył.* | Produkt.* | Towar.*'
        )
        return item_loader.load_item()
