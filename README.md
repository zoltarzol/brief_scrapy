# brief_scrapy

On top 250 films page:
	start_urls = ['https://www.imdb.com/chart/top/']

Release year:
	response.xpath('//*[@class="secondaryInfo"]/text()').get()[1:-1]

Title
	response.xpath('//*[@class="titleColumn"]/text()').get()

On movie details page:
	start_urls = ['https://www.imdb.com/title/tt0111161']
	
Langue origine
	response.xpath('//a[@class="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"]/text()').getall()[16]