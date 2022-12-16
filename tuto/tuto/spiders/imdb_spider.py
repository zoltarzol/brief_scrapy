import scrapy, re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from tuto.items import IMDBMovie
#from scrapy.http import HtmlResponse
# from dataclasses import dataclass, field
# from typing import Optional

class IMDBSpider(CrawlSpider):
    name = "IMDB"

    allowed_domains = ['imdb.com']

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

    start_urls = ['https://www.imdb.com/chart/top/']

    custom_settings = {
    # spécifie l'ordre d'export des attributs de IMDBMovie (dans le CSV résultant par exemple)
    'FEED_EXPORT_FIELDS': ["title","original_title","score","genres","release_year","length_in_minutes","synopsis","directors","actors","public","countries_of_origin","original_languages"],
    }

    lang = 'en-US'

    limit = 260

    # movies = [IMDBMovie()]

    top_movies_page = LinkExtractor(restrict_xpaths="//td[@class='titleColumn']/a")

    movie_details_page = LinkExtractor(restrict_xpaths='//section[@class="ipc-page-background ipc-page-background--baseAlt sc-9497c711-0 fZhWtO"]')

    rule_top_movies_page = Rule(top_movies_page,
                             callback='parse_items',
                              follow=False)
    
    rule_movie_details_page = Rule(movie_details_page,
                            callback='parse_items',
                            follow=False)
                            
    rules = (
      rule_top_movies_page, rule_movie_details_page
    )

    def start_requests(self):
        urls = self.start_urls
        for url in urls:
            yield scrapy.Request(url=url, headers={'User-Agent': self.user_agent , 'Accept-Language': self.lang })

    def parse_items(self, response):
        print(response._get_url())
             
        scrape_count = self.crawler.stats.get_value('item_scraped_count')
        if scrape_count == self.limit:
            raise CloseSpider("Limit reached")
        
        title = response.xpath('//*[contains(concat(" ", @data-testid, " "), "hero-title-block__title")]/text()').get()
        print("rank:",scrape_count,"\nTitle:",title)

        original_title_temp = response.xpath('//*[contains(concat(" ", @class, " "), "gwBsXc")]/text()').get()

        if original_title_temp == None:
            original_title = original_title_temp
        else:
            original_title = original_title_temp[16:]
        
        score = float(response.xpath('//*[contains(concat(" ", @class, " "), "jGRxWM")]/text()').getall()[0])
        # print(score)

        genres = response.xpath('//a[contains(concat(" ", @class, " "), "bYNgQ")]/span[@class="ipc-chip__text"]/text()').getall()
        # print(genres)

        release_year = int(response.xpath('//a[contains(concat(" ", @class, " "), "WIUyh")]/text()').getall()[0].strip('()'))
        # print(release_year)

        tmp = response.xpath('//ul[contains(concat(" ", @class, " "), "kqWovI")]/li[@class="ipc-inline-list__item"]/text()').getall()
        if len(tmp)>2:
            length_in_minutes = int(tmp[0])*60 + int(tmp[3])
        else:
            length_in_minutes = int(tmp[0])
        # print(length_in_minutes)

        synopsis = response.xpath('//*[contains(concat(" ", @class, " "), "gXUyNh")]/text()').getall()[0]
        # print(synopsis)

        directors = response.xpath('//div[contains(concat(" ", @class, " "), "fjLeDR")]//a[contains(concat(" ", @href, " "), "tt_ov_dr")]/text()').getall()
        # print(directors)
        
        actors = response.xpath('//a[@data-testid="title-cast-item__actor"]/text()').getall()
        # print(actors)

        public_temp = response.xpath('//a[contains(concat(" ", @class, " "), "WIUyh")]/text()').getall()
        print(public_temp)

        if not public_temp:
            public = public_temp
        else:
            try:
                public = public_temp[1]
            except IndexError:
                public = public_temp[0]

        countries_of_origin = response.xpath('//a[contains(concat(" ", @href, " "), "country_of_origin")]/text()').getall()
        # print(countries_of_origin)

        original_languages = response.xpath('//a[contains(concat(" ", @href, " "), "primary_language")]/text()').getall()
        # print(original_languages)
        
        movie_item = IMDBMovie(title=title,original_title=original_title,score=score,genres=genres,release_year=release_year,length_in_minutes=length_in_minutes,synopsis=synopsis,directors=directors,actors=actors,public=public,countries_of_origin=countries_of_origin,original_languages=original_languages)
        
        yield movie_item

    # def parse(self, response):
    #     yield response._get_url()

    # # premiers tests, avant l'utilisation de parse_items    
    # def parse(self, response):
    #     print(response._get_url())
    #     temp = response.xpath('//div[contains(concat(" ", @class, " "), "fjLeDR")]//a[contains(concat(" ", @href, " "), "tt_ov_dr")]/text()').getall()
        
    #     print("----------------------------------------------------")
    #     print(temp)
    #     print("----------------------------------------------------")


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
        
    