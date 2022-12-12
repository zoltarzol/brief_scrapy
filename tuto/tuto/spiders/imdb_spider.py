import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class IMDBMovie:
    title: Optional[str] = field(default=None)
    original_title: Optional[str] = field(default=None)
    score: Optional[float] = field(default=None)
    genre: Optional[str] = field(default=None)
    date: Optional[int] = field(default=None)
    length_in_minutes: Optional[int] = field(default=None)
    synopsis: Optional[str] = field(default=None)
    directors: Optional[list(str)] = field(default=None)
    actors: Optional[list(str)] = field(default=None)
    mpaa: 


class IMDBSpider(CrawlSpider):
    name = "IMDB"
    allowed_domains = ['imdb.com']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    start_urls = ['https://www.imdb.com/chart/top/']
    lang = 'fr-FR'
    itertag = 'item'

    def start_requests(self):
        urls = [
            'https://www.imdb.com/chart/top/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={'User-Agent': self.user_agent , 'Accept-Language': self.lang })

    # def parse(self, response):
    #     item = scrapy.Item()
    #     item['rank'] = response.xpath('//div[@class="lister"]/text()')
    #     item['name'] = response.xpath('//td[@id="item_name"]/text()').get()
    #     item['description'] = response.xpath('//td[@id="item_description"]/text()').get()
    #     item['link_text'] = response.meta['link_text']


    def parse(self, response):
        item = IMDBMovie()
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        item['title'] = response.xpath('//td[@class="titleColumn"]/text').get()
        print(item['title'])
        # print(response.xpath('//td[@class="titleColumn"]').getall())
        # print(response.xpath('//span[@class="secondaryInfo"]').get())

        # item["releaseDate"] = response.xpath('//span[@class="secondaryInfo"]').get()
        # print(item["rank_name_year"])
        # item['name'] = response.xpath('//td[@id="item_name"]/text()').get()
        # item['description'] = response.xpath('//td[@id="item_description"]/text()').get()
        # item['link_text'] = response.meta['link_text']
