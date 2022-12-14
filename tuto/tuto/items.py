# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class IMDBMovie(scrapy.Item):
    # rank n'est pas demandé dans les consignes, mais je le scrape et l'enregistre pour le côté pratique, car si les données finissent mélangées, le score avec une seule décimale ne permettra pas de reconstituer la liste dans l'ordre. Le rank pourrait bien évidemment être généré à la volée avec un range(1,250) plutôt que via scraping, mais un petit défi technique (expliqué plus bas) m'a poussé à chercher une solution réutilisable pour ce genre de situations.
    rank = scrapy.Field()
    title = scrapy.Field()
    original_title = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    release_date = scrapy.Field()
    length_in_minutes = scrapy.Field()
    synopsis = scrapy.Field()
    # ce sera une liste car certains films ont plusieurs réalisateurs
    directors = scrapy.Field()
    actors = scrapy.Field()
    public = scrapy.Field()
    country_of_origin = scrapy.Field()
    # ce sera une liste car certains films sont d'origine dans plusieurs langues
    original_languages = scrapy.Field()