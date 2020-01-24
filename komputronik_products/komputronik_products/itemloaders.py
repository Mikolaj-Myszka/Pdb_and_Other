from scrapy.loader import ItemLoader


def name_availability_processor(self, values):
    for v in values:
        yield v.strip()


def price_processor(self, values):
    for v in values:
        yield "".join(v.split())


class KomputronikItemLoader(ItemLoader):

    name_in = name_availability_processor
    price_in = price_processor
    availability_in = name_availability_processor
