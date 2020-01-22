# -*- coding: utf-8 -*-

import scrapy
from komputronik_products.itemloaders import KomputronikItemLoader
from komputronik_products.items import KomputronikProductsItem
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Compose


class KomputronikProductSpider(scrapy.Spider):
    name = 'komputronik_product'
    start_urls = [
        'https://www.komputronik.pl/product/633622/lenovo-ideapad-330-15arr-\
            81d200n7pb-120gb-ssd.html',
        'https://www.komputronik.pl/product/675464/lenovo-ideapad-s145-15api-\
            81ut0068pb-8gb.html',
        'https://www.komputronik.pl/product/666766/lenovo-ideapad-s145-14iwl-\
            81mu009tpb-.html',
    ]

    def parse(self, response):
        
        item_loader = KomputronikItemLoader(
            item=KomputronikProductsItem(), response=response
        )
        
        # name = response.xpath('//h1/text()')[0].extract().strip()
        
        item_loader.add_xpath('name', '//h1/text()')
        
        # price = "".join(response.xpath(
        #     '//span[@class="proper"]/text()')[0].extract().split()
        # )
        
        item_loader.add_xpath('price', '//span[@class="proper"]/text()', TakeFirst())
        
        # availability = response.xpath(
        #     '//a[@class="tooltip-wrap pretty"]/text()'
        # )[1].extract().strip()
        
        item_loader.add_xpath('availability', '//a[@class="tooltip-wrap pretty"]/text()', re='Wysyłamy .* | Produkt .*')
        
        return item_loader.load_item()
