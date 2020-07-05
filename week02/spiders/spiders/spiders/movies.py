import scrapy
from SpidersItem.items import SpidersItem
from scrapy.selector import  Selector

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']


    def start_requests(self):
        for i in range(1):
            url = 'https://maoyan.com/films?showType=3&offset='+str(30*i)
            yield scrapy.Request(url=url , callback=self.parse)

    def parse(self, response):

        movies = Selector(response=response).xpath("//div[@class=\"movie-hover-info\"]")
        for movie in movies:
            item = SpidersItem()
            name = movie.xpath('./div[1]/span/text()').extract()
            classification = movie.xpath('./div[2]/text()').extract()[1].strip('\n').strip()
            display_time = movie.xpath('./div[4]/text()').extract()[1].strip('\n').strip()
            item['movie_name'] = name
            item['movie_type'] = classification
            item['movie_time']  = display_time
            yield  item