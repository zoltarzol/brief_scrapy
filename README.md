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



<td class="titleColumn">
      1.
      <a href="/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&amp;pf_rd_r=Y2GTPN0DEGZKVKSDAWA6&amp;pf_rd_s=center-1&amp;pf_rd_t=15506&amp;pf_rd_i=top&amp;ref_=chttp_tt_1" title="Frank Darabont (dir.), Tim Robbins, Morgan Freeman">The Shawshank Redemption</a>
        <span class="secondaryInfo">(1994)</span>
    </td>