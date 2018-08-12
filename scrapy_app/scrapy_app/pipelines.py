# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from main.models import Quote


class ScrapyAppPipeline(object):
    def process_item(self, item, spider):
        quote = Quote(text=item.get('text'), author=item.get('author'))
        quote.save()
        return item
