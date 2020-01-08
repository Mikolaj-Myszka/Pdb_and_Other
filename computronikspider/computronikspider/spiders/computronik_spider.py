# -*- coding: utf-8 -*-
import scrapy
from ..items import ComputronikspiderItem
import csv


class ComputronikSpiderSpider(scrapy.Spider):
    name = 'computronik_spider'
    start_urls = ['https://www.komputronik.pl/category/5022/laptopy.html?\
        pr10%5B%5D=0&pr10%5B%5D=1500&prod%5B%5D=23&filter=1&showBuyActiveOnly=0&\
        sort=1&by=f_price_10&showProducts=1']
    page_number = 2

    with open('csv_komputronik.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([
            'product_name',
            'product_price [zl]',
            'product_availability'
        ])

    def parse(self, response):
        item = ComputronikspiderItem()

        all_products = response.css('li.product-entry2')
        print('---> Length:', len(all_products))

        with open('csv_komputronik.csv', 'a', newline='') as csvfile:
            for product in all_products:
                csvwriter = csv.writer(csvfile, delimiter=',')
                some_text = product.css('.blank-link::text')[0].extract()

                if '{{::' not in some_text:

                    # product_name
                    product_name = some_text.strip()

                    # product_price
                    some_text = product.css('.proper::text')[0].extract()
                    product_price = some_text.strip().replace('\xa0', '')

                    # product_availability
                    some_text = product.css('.bdg-label::text')[0].extract()
                    product_availability = some_text.strip()

                    item['product_name'] = product_name
                    item['product_price'] = product_price
                    item['product_availability'] = product_availability

                    csvwriter.writerow([
                        product_name,
                        product_price,
                        product_availability,
                    ])

                    yield item

        # option to crawl next pages
        next_page = self.start_urls[0] + '&p=' + str(self.page_number)

        if len(all_products) > 1:
            self.page_number += 1
            yield response.follow(next_page, callback=self.parse)
