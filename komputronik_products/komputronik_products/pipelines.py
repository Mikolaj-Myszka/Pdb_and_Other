# -*- coding: utf-8 -*-

from scrapy.exporters import CsvItemExporter


class KomputronikProductsPipeline(object):
    """Distribute items across multiple CSV files
    according to their 'name' field
    """

    product_file = open('komputronik_products.csv', 'wb')

    def open_spider(self, spider):
        self.product_to_exporter = {}

    def close_spider(self, spider):
        for exporter in self.product_to_exporter.values():
            exporter.finish_exporting()
            self.product_file.close()

    def _exporter_for_item(self, item):
        product_name = item['name'][0]
        exporter = CsvItemExporter(self.product_file, include_headers_line=False)
        exporter.start_exporting()
        self.product_to_exporter[product_name] = exporter
        return self.product_to_exporter[product_name]

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item
