# -*- coding: utf-8 -*-
import scrapy
from ..items import ComputronikspiderItem


class ComputronikSpiderSpider(scrapy.Spider):
    name = 'computronik_spider'
    start_urls = ['https://www.komputronik.pl/category/5022/laptopy.html?pr10%5B%5D=0&pr10%5B%5D=1500&prod%5B%5D=23&filter=1&showBuyActiveOnly=0&sort=1&by=f_price_10&showProducts=1']
    page_number = 2

    def parse(self, response):
        item = ComputronikspiderItem()

        all_products = response.css('li.product-entry2')
        # print(all_products)
        print('---> Length:', len(all_products))

        
        for product in all_products:

            some_text = product.css('.blank-link::text')[0].extract()

            if '{{::' not in some_text:

                # print(some_text)
                product_name = some_text.strip()
                # print(product_name)

                some_text = product.css('.proper::text')[0].extract()
                # print(some_text))
                product_price = some_text.strip().replace('\xa0', '')
                # print(product_price)

                some_text = product.css('.bdg-label::text')[0].extract() # <- wybiera pierwsze
                # print(some_text)
                product_availability = some_text.strip()
                # print(product_availability)


                item['product_name'] = product_name
                item['product_price'] = product_price
                item['product_availability'] = product_availability

                yield item

        """
        next_page = self.start_urls[0] + '&p=' + str(self.page_number)

        if len(all_products) > 1:
            self.page_number += 1
            yield response.follow(next_page, callback=self.parse)
        """
        
        
        """
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
            some_text[i] = some_text[i].replace('\n'
                          '                                    ', '').replace('                                ', '')
            if ('Dostawa' not in some_text[i]) and (some_text[i] != '!\n') \
                and ('Do odbioru' not in some_text[i]) \
                and ('Wysył' not in some_text[i]) \
                and ('{{::' not in some_text[i]):
                product_availability.append(some_text[i])


        item['product_name'] = product_name
        item['product_price'] = product_price
        item['product_availability'] = product_availability

        # print('hoh', len(item['product_availability']))
        """

        
        
