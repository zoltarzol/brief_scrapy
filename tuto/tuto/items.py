import scrapy

class IMDBMovie(scrapy.Item):
    # rank n'est pas demandé dans les consignes, mais je le scrape et l'enregistre pour le côté pratique, car si les données finissent  élangées, le score avec une seule décimale ne permettra pas de reconstituer la liste dans l'ordre. Le rank pourrait bien évidemment être généré à la volée avec un range(1,250) plutôt que via scraping, mais un petit défi technique (expliqué plus bas) m'a poussé à chercher une solution réutilisable pour ce genre de situations.

    ####################################
    # Finalement le temps m'a manqué...#
    ####################################

    # rank = scrapy.Field()

    title = scrapy.Field()

    original_title = scrapy.Field()

    score = scrapy.Field()

    #liste car certains films ont plusieurs genres
    genres = scrapy.Field()

    release_year = scrapy.Field()

    length_in_minutes = scrapy.Field()
    
    synopsis = scrapy.Field()

    # liste car certains films ont plusieurs réalisateurs
    directors = scrapy.Field()
    
    # liste également
    actors = scrapy.Field()

    public = scrapy.Field()

    # liste également
    countries_of_origin = scrapy.Field()

    # liste également car certains films sont dans plusieurs langues
    original_languages = scrapy.Field()