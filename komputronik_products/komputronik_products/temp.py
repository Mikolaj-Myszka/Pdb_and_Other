# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from scrapy.loader.processors import TakeFirst
from komputronik_products.itemloaders import KomputronikItemLoader
from komputronik_products.items import KomputronikProductsItem


class KomputronikProductSpider(scrapy.Spider):
    name = 'komputronik_product'
    
    start_urls = [
        'https://www.komputronik.pl/category/5022/laptopy.html?pr10%5B%5D=0\
            &pr10%5B%5D=1400&prod%5B%5D=23&filter=1&showBuyActiveOnly=0\
            &sort=1&by=f_price_10&showProducts=1',
    ]

    page_number = 1
    print(page_number)
    last_page = 0
    all_products_links = []
    i = 0
    """
    start_urls = [
        'https://www.komputronik.pl/product/633622/lenovo-ideapad-330-15arr-\
            81d200n7pb-120gb-ssd.html',
        'https://www.komputronik.pl/product/675464/lenovo-ideapad-s145-15api-\
            81ut0068pb-8gb.html',
        'https://www.komputronik.pl/product/666766/lenovo-ideapad-s145-14iwl-\
            81mu009tpb-.html',
    ]
    """

    def parse(self, response):
        
        if self.page_number == 1:
            self.last_page = int(response.css('.pgn-static+ li a::text')[0].extract())
            print('last_page:', self.last_page)
        
        
        if self.page_number <= self.last_page:
            page_links = response.xpath('//div[@class="pe2-head"]//a/@href').extract()
            #print(page_links)
            self.all_products_links.extend(page_links)
            # print(self.all_products_links)
            print(len(self.all_products_links))

            self.page_number += 1
            print(self.page_number)
            next_page = self.start_urls[0] + '&p=' + str(self.page_number)
            
            if self.page_number == self.last_page:
                # print('parse_products')
                # self.parse_products(response)
                next_page = self.all_products_links[self.i]
                yield response.follow(next_page, callback=self.parse_products)
            else:
                yield response.follow(next_page, callback=self.parse)
        


    def loading_product_items(self,response):
        print('hello')
        item_loader = KomputronikItemLoader(
            item=KomputronikProductsItem(), response=response
        )
        item_loader.add_xpath('name', '//h1/text()')
        item_loader.add_xpath('price', '//span[@class="proper"]/text()', TakeFirst())
        item_loader.add_xpath('availability', '//a[@class="tooltip-wrap pretty"]/text()', re='Wysyłamy.* | Produkt.*')
        return item_loader.load_item()



    def parse_products(self, response):

        self.loading_product_items(response)

        if self.i < len(self.all_products_links)-1:
            print('hello2')
            self.i += 1
            next_page = self.all_products_links[self.i]
            yield response.follow(next_page, callback=self.parse_products)



        """
        for i in range(0, len(self.all_products_links)):
            print(i)
            request = Request(url=self.all_products_links[i])
        
            item_loader = KomputronikItemLoader(
                item=KomputronikProductsItem(), response=response
            )
            item_loader.add_xpath('name', '//h1/text()')
            item_loader.add_xpath('price', '//span[@class="proper"]/text()', TakeFirst())
            item_loader.add_xpath('availability', '//a[@class="tooltip-wrap pretty"]/text()', re='Wysyłamy.* | Produkt.*')

            return item_loader.load_item()
        """





        
        """
        else:
            item_loader = KomputronikItemLoader(
                item=KomputronikProductsItem(), response=response
            )
            item_loader.add_xpath('name', '//h1/text()')
            item_loader.add_xpath('price', '//span[@class="proper"]/text()', TakeFirst())
            item_loader.add_xpath('availability', '//a[@class="tooltip-wrap pretty"]/text()', re='Wysyłamy.* | Produkt.*')
            
            if self.i < len(self.all_products_links)-1:
                self.i += 1
                next_page = self.all_products_links[self.i]
                item_loader.load_item()
                yield response.follow(next_page, callback=self.parse)
        """
        
        """
        item_loader = KomputronikItemLoader(
            item=KomputronikProductsItem(), response=response
        )
        item_loader.add_xpath('name', '//h1/text()')
        item_loader.add_xpath('price', '//span[@class="proper"]/text()', TakeFirst())
        item_loader.add_xpath('availability', '//a[@class="tooltip-wrap pretty"]/text()', re='Wysyłamy.* | Produkt.*')
        return item_loader.load_item()
        """

# https://stackoverflow.com/questions/29749854/scrapy-calling-another-url