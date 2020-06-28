# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas



		


class SpidersPipeline:

    def process_item(self, item, spider):
        name = item['name'][0]
        display_time = item['display_time']
        classification = item['classification']
        movie = pandas.DataFrame([(name,classification,display_time)])
        movie.to_csv('./movies.csv',mode='a',encoding='utf-8')
        return item
