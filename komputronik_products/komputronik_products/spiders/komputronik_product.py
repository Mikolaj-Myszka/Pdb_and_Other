# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from komputronik_products.items import KomputronikProductsItem


class KomputronikProductSpider(scrapy.Spider):
    name = 'komputronik_product'
    start_urls = [
        'https://www.komputronik.pl/product/633622/lenovo-ideapad-330-15arr-81d200n7pb-120gb-ssd.html', 
        'https://www.komputronik.pl/product/675464/lenovo-ideapad-s145-15api-81ut0068pb-8gb.html',
        'https://www.komputronik.pl/product/633622/lenovo-ideapad-330-15arr-81d200n7pb-120gb-ssd.html',
        'https://www.komputronik.pl/product/675464/lenovo-ideapad-s145-15api-81ut0068pb-8gb.html',
    ]

    def parse(self, response):
        l = ItemLoader(item=KomputronikProductsItem(), response=response)
        name = response.xpath('//h1/text()')[0].extract().strip()
        l.add_value('name', name)
        price = response.xpath('//span[@class="proper"]/text()')[0].extract().strip()
        l.add_value('price', price)
        availability = response.xpath('//a[@class="tooltip-wrap pretty"]/text()')[1].extract().strip()
        l.add_value('availability', availability)
        return l.load_item()