from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


# def strip_dashes(x):
#     return x.strip('-')

def name_processor(self, values):
    for v in values:
        yield v.strip()

def price_processor(self, values):
    for v in values:
        yield "".join(v.split())

def availability_processor(self, values):
    for v in values:
        yield v.strip()


class KomputronikItemLoader(ItemLoader):

    name_in = name_processor
    price_in = price_processor
    availability_in = availability_processor

    

    # default_output_processor = TakeFirst()

    # name = response.xpath('//h1/text()')[0].extract().strip()

    # name_in = MapCompose(unicode.title)
    # name_in = Compose(lambda v: v[0], str.lower)
    # name_out = Join()

    # price_in = MapCompose(unicode.strip)

    #['the', 'prevoius']
    # ['The', 'Previus']
    # 'ThePrevius'