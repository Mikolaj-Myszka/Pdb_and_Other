# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

"""
class KomputronikProductsPipeline(object):
    def process_item(self, item, spider):
        return item
"""

from scrapy.exporters import CsvItemExporter

class KomputronikProductsPipeline(object):
    """Distribute items across multiple XML files according to their 'year' field"""

    def open_spider(self, spider):
        self.year_to_exporter = {}

    def close_spider(self, spider):
        for exporter in self.year_to_exporter.values():
            exporter.finish_exporting()

    def _exporter_for_item(self, item):
        year = item['name'][0]
        if year not in self.year_to_exporter:
            f = open('{}.csv'.format(year), 'wb')
            exporter = CsvItemExporter(f)
            exporter.start_exporting()
            self.year_to_exporter[year] = exporter
        return self.year_to_exporter[year]

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item
