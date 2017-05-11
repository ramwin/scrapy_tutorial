# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyTutorialPipeline(object):
    def process_item(self, item, spider):
        self.file.write("%s: %s\n" % (item["id"], item["text"]))
        return item

    def open_spider(self, spider):
        self.file = open("data.txt", "w")

    def close_spider(self, spider):
        import datetime
        self.file.write("%s\n" % datetime.datetime.now().isoformat())
        self.file.close()
