# brief_scrapy

```
On top 250 films page:
	start_urls = ['https://www.imdb.com/chart/top/']

Release year:
	response.xpath('//*[@class="secondaryInfo"]/text()').get()[1:-1]

Title
	response.xpath('//*[@class="titleColumn"]/text()').get()

On movie details page:
	start_urls = ['https://www.imdb.com/title/tt011111']
	
Langue origine
	response.xpath('//a[@class="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link"]/text()').getall()[16]

Per movie page:

title = response.xpath('//*[contains(concat(" ", @class, " "), "eKrKux")]/text()').getall()[0]

original_title = re.findall(': (.*)',response.xpath('//*[contains(concat(" ", @class, " "), "gwBsXc")]/text()').getall()[0])
score = response.xpath('//*[contains(concat(" ", @class, " "), "jGRxWM")]/text()').getall()[0]

genres = response.xpath('//a[contains(concat(" ", @class, " "), "bYNgQ")]/span[@class="ipc-chip__text"]/text()').getall()

release_year = response.xpath('//a[contains(concat(" ", @class, " "), "WIUyh")]/text()').getall()[0].strip('()')

temp = response.xpath('//ul[contains(concat(" ", @class, " "), "kqWovI")]/li[@class="ipc-inline-list__item"]/text()').getall()
        if(len(temp)>2):
            length_in_minutes = int(temp[0])*60 + int(temp[3])
        else:
            length_in_minutes = int(temp[0])

synopsis = response.xpath('//*[contains(concat(" ", @class, " "), "gXUyNh")]/text()').getall()[0]

directors = response.xpath('//div[contains(concat(" ", @class, " "), "fjLeDR")]//a[contains(concat(" ", @href, " "), "tt_ov_dr")]/text()').getall()
actors = response.xpath('//a[@data-testid="title-cast-item__actor"]/text()').getall()

public = response.xpath('//a[contains(concat(" ", @class, " "), "WIUyh")]/text()').getall()[1]

countries_of_origin (list) = response.xpath('//a[contains(concat(" ", @href, " "), "country_of_origin")]/text()').getall()

original_languages = response.xpath('//a[contains(concat(" ", @href, " "), "primary_language")]/text()').getall()
```

```
------
CONFIG
------

sudo apt update
sudo apt upgrade
sudo apt --fix-broken install
conda install importlib-metadata  
conda install -c plotly plotly_express
conda install mongodb-compass
conda install networkx
conda install seaborn
pip3 install 'pymongo[srv]'

--on tente
conda install streamlit

--sinon
pip install streamlit==1.12.0
pip install streamlit --upgrade
```