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

Per movie page:

rank = 
title = eKrKux
original_title = 
score = 
genre = 
release_year = WIUyh[0]
length_in_minutes = 
synopsis = 
directors = 
actors = response.xpath('//a[@data-testid="title-cast-item__actor"]/text()').getall()
public = WIUyh[1]
country_of_origin (list) = response.xpath('//a[contains(concat(" ", @href, " "), "country_of_origin")]/text()').getall()
original_languages = response.xpath('//a[contains(concat(" ", @href, " "), "primary_language")]/text()').getall()


<td class="titleColumn">
      1.
      <a href="/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&amp;pf_rd_r=Y2GTPN0DEGZKVKSDAWA6&amp;pf_rd_s=center-1&amp;pf_rd_t=15506&amp;pf_rd_i=top&amp;ref_=chttp_tt_1" title="Frank Darabont (dir.), Tim Robbins, Morgan Freeman">The Shawshank Redemption</a>
        <span class="secondaryInfo">(1994)</span>
    </td>


how can I host my files on atlas using mongoDB? explain step by step with details.

1. Create an Atlas Account: The first step to hosting files on Atlas is to create an account at MongoDB Atlas. This can be done by visiting the MongoDB Atlas website and clicking the "Get Started Free" button.

2. Create a Cluster: Once you have an account, you'll need to create a cluster in Atlas. A cluster is a group of MongoDB servers that act as one. You can create a cluster by clicking the "Build a Cluster" button on the Atlas dashboard.

3. Connect to the Cluster: Once the cluster is created, you'll need to connect to it. To do this, click the "Connect" button on the cluster's page. This will open a dialog box that allows you to connect to the cluster via a secure shell (SSH).

4. Upload Your Files: Now that you're connected to the cluster, you can upload your files. This can be done by clicking the "Upload" button on the cluster's page and selecting the files you'd like to upload.

5. Access Your Files: Once your files have been uploaded, they will be accessible in the cluster. You can access them by clicking the "Data" tab on the cluster's page and selecting the appropriate collection. From here, you'll be able to view, edit, and delete your files.