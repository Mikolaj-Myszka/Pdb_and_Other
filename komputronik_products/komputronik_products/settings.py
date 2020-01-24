
BOT_NAME = 'komputronik_products'

SPIDER_MODULES = ['komputronik_products.spiders']
NEWSPIDER_MODULE = 'komputronik_products.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'komputronik_products.pipelines.KomputronikProductsPipeline': 300,
}
