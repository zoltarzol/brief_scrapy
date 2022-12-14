import scrapy, re
from scrapy.spiders import CrawlSpider
from scrapy.http import HtmlResponse
# from dataclasses import dataclass, field
# from typing import Optional

class IMDBMovie(scrapy.Item):
    title = scrapy.Field()
    # non demandé dans les consignes, mais scrapé par acquis de conscience, car si les données finissent mélangées, le score avec une seule décimale ne permettra pas de reconstituer la liste dans l'ordre
    rank = scrapy.Field()
    # original_title = scrapy.Field()
    # score = scrapy.Field()
    # genre = scrapy.Field()
    release_date = scrapy.Field()
    # length_in_minutes = scrapy.Field()
    # synopsis = scrapy.Field()
    # # ce sera une liste car certains films ont plusieurs réalisateurs
    # directors = scrapy.Field()
    # actors = scrapy.Field()
    # public = scrapy.Field()
    # country_of_origin = scrapy.Field()
    # # ce sera une liste car certains films sont d'origine dans plusieurs langues
    # original_languages = scrapy.Field()
    

class IMDBSpider(CrawlSpider):
    name = "IMDB"
    allowed_domains = ['imdb.com']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    start_urls = ['https://www.imdb.com/chart/top/']
    custom_settings = {
    # spécifie l'ordre d'export des attributs de IMDBMovie dans le CSV résultant
    'FEED_EXPORT_FIELDS': ["title", "rank", "release_date"],
    }

    lang = 'fr-FR'
    movies = [IMDBMovie()]

    def start_requests(self):
        urls = self.start_urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={'User-Agent': self.user_agent , 'Accept-Language': self.lang })
    
    def parse(self, response):
        for title, release_date in zip(
            response.xpath('//td[@class="titleColumn"]/a/text()').getall(),
            response.xpath('//span[@class="secondaryInfo"]/text()').getall():
            for a in response.xpath('//*[@class="titleColumn"]/text()'):
                print(a)
            # .xpath('//*[@class="titleColumn"]/text()').text_content()):
            # print(len(rank))
            movie_item = IMDBMovie(title=title, release_date=release_date.strip('()'), rank=rank)
            yield movie_item

        # movies = [IMDBMovie()]
        # movies[0]['title'] = []
        # movies[0]['title'].extend(['toto'])
        # print(movies[0]['title'][0])