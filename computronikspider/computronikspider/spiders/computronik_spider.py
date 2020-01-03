# -*- coding: utf-8 -*-
import scrapy
from ..items import ComputronikspiderItem


class ComputronikSpiderSpider(scrapy.Spider):
    name = 'computronik_spider'
    start_urls = ['https://www.komputronik.pl/category/5022/laptopy.html?pr10%5B%5D=0&pr10%5B%5D=4000&prod%5B%5D=23&filter=1&showBuyActiveOnly=0&sort=1&by=f_price_10&showProducts=1']

    def parse(self, response):
        item = ComputronikspiderItem()

        # product_name
        product_name = []
        some_text = response.css('.blank-link::text').extract()[11:31]
        for i in range(0, len(some_text)):
            product_name.append(some_text[i].replace('\n'
                  '                    ', '').replace('                ', ''))

        # product_price
        product_price = []
        some_text = response.css('.proper::text').extract()
        for i in range(0, len(some_text), 2):
            product_price.append(some_text[i].replace('\xa0', '').replace('\n                ', ''))

        # product_availability
        product_availability = []
        some_text = response.css('.bdg-label::text').extract()
        for i in range(0, len(some_text)):
            product_availability.append(some_text[i].replace('\n'
                          '                                    ', '').replace('                                ', ''))


        item['product_name'] = product_name
        item['product_price'] = product_price
        item['product_availability'] = product_availability

        print(len(item['product_availability']))
        """
        for i in range(0, len(product_name)):
            print(i, product_name[i])
        """

        yield item
        
