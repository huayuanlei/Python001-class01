# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class CatMoviePipeline:
    def process_item(self, item, spider):
        movie_xpath = pd.DataFrame(data=item)
        movie_xpath.to_csv('./movie_spider.csv', encoding='utf-8', index=False, header=0, mode="a")

