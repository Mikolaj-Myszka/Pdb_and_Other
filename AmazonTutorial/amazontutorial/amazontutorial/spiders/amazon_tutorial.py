# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem


class AmazonTutorialSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011'
    ]

    def parse(self, response):
        item = AmazontutorialItem()

        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        item['product_name'] = product_name
        item['product_author'] = product_author
        item['product_price'] = product_price
        item['product_imagelink'] = product_imagelink

        yield item
