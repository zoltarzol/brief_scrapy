import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import HtmlResponse
# from dataclasses import dataclass, field
# from typing import Optional

class IMDBMovie(scrapy.Item):
    title = scrapy.Field()
    original_title = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    release_date = scrapy.Field()
    length_in_minutes = scrapy.Field()
    synopsis = scrapy.Field()
    directors = [scrapy.Field()]
    actors = scrapy.Field()

class IMDBSpider(CrawlSpider):
    name = "IMDB"
    allowed_domains = ['imdb.com']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    start_urls = ['https://www.imdb.com/chart/top/']
    lang = 'fr-FR'
    movies = [IMDBMovie()]

    def start_requests(self):
        urls = [
            # 'https://www.imdb.com/chart/top/',
            'https://www.imdb.com/title/tt0111161',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={'User-Agent': self.user_agent , 'Accept-Language': self.lang })
    
    def parse(self, response):
        print(response.xpath('//a[@class="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"]/text()').getall()[16])
        # for movie in response.xpath('//div[@class="lister"]').getall():
        #     self.movies.append(IMDBMovie(
        #         title = HtmlResponse(movie).xpath('//*[@class="titleColumn"]/text()').get(),
        #         release_date = HtmlResponse(movie).xpath('//*[@class="secondaryInfo"]/text()').get()
        #         ))
        #     yield movie

            

        # movies = [IMDBMovie()]
        # movies[0]['title'] = []
        # movies[0]['title'].extend(['toto'])
        # print(movies[0]['title'][0])