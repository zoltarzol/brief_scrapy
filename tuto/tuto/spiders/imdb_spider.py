import scrapy #, re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tuto.items import IMDBMovie
from scrapy.exceptions import CloseSpider
# from scrapy.http import HtmlResponse
# from dataclasses import dataclass, field
# from typing import Optional

class IMDBSpider(CrawlSpider):
    name = "IMDB"
    allowed_domains = ['imdb.com']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    start_urls = ['https://www.imdb.com/chart/top/']
    custom_settings = {
    # spécifie l'ordre d'export des attributs de IMDBMovie (dans le CSV résultant par exemple)
    'FEED_EXPORT_FIELDS': ["title"],
    }
    lang = 'en-US'
    limit = 10
    movies = [IMDBMovie()]

    # rules = (
    #     Rule(LinkExtractor(allow=(), restrict_xpaths=('//td[@class="titleColumn"]/a',)), callback="parse_items", follow= False),
    # )

    def start_requests(self):
        urls = self.start_urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={'User-Agent': self.user_agent , 'Accept-Language': self.lang })

    def parse_items(self, response):
        scrape_count = self.crawler.stats.get_value('item_scraped_count')
        if scrape_count == self.limit:
            raise CloseSpider("Limit of",self.limit,"items reached")
        
    # premiers tests, avant l'utilisation de parse_items    
    def parse(self, response):
        country_of_origin = response.xpath('//td[@class="titleColumn"]/a/text()').getall()
        print(country_of_origin)





        # # Pour pour tard : problème non résolu de la récupération du rank dans le code HTML
        # # Le souci vient de passages à la ligne à l'intérieur des balises que vise le XPath
        # # Cela engendre la récupération par getall() de 3 champs pour 1 réel, et donc d'un
        # # total de 750 champs au lieu des 250 visés.
        # # Le XPath utilisé est le suivant : response.xpath('//*[@class="titleColumn"]/text()')
        # # Le problème (ou plutôt la limitation, car dans la philosophie Scrapy, c'est un résultat
        # # attendu) est connue et référencée dans le GitHub de Scrapy :
        # # https://github.com/scrapy/parsel/issues/128
        # # Ma solution de contournement se trouve ci-dessous.

        # rank_list_with_newline_elements_to_remove = response.xpath('//td[@class="titleColumn"]/text()').getall()
        # rank_list_cleaned = [i.strip().replace('\n','').replace('.','') for i in rank_list_with_newline_elements_to_remove[::3]]

        # for title, release_year, rank in zip(
        #     response.xpath('//td[@class="titleColumn"]/a/text()').getall(),
        #     response.xpath('//span[@class="secondaryInfo"]/text()').getall(),
        #     rank_list_cleaned):
        #     movie_item = IMDBMovie(title=title, release_year=release_year.strip('()'), rank=rank)
        #     yield movie_item