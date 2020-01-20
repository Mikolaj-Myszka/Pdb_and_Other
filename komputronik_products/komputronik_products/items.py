# -*- coding: utf-8 -*-

import scrapy


class KomputronikProductsItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()
