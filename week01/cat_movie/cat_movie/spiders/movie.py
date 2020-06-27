import scrapy
from cat_movie.items import CatMovieItem
import lxml.etree


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = "https://maoyan.com/films?showType=3"
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        bs_info = lxml.etree.HTML(response.text)
        items = []
        for list in range(1, 11):
            item = CatMovieItem()
            name_movie = bs_info.xpath(f'//a[{list}]/div/div[2]/div[1]/text()')
            style_movie = bs_info.xpath(f'//a[{list}]/div/div[2]/div[3]/text()')
            time_movie = bs_info.xpath(f'//a[{list}]/div/div[2]/div[4]/text()')
            item["name_movie"] = name_movie
            item["style_movie"] = style_movie
            item["time_movie"] = time_movie
            items.append(item)
            yield items


