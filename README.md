scrapy-mobile_de
================

is framework for scraping mobile.de web site and sending out email when new ad for given criteria appears. This is important since good cars are sold instantly

install
=======
this is complete scrapy project and you need only running version of scrapy (>=0.14) in order to run it:

git clone https://github.com/whiskeykontequila/scrapy-mobile_de.git

Configure from_email, to_emails and start_urls in mobile_de/spiders/mobile_de_spider.py
start_url you get by going to mobile.de, configuring search criteria and copy&pasting url from your browser into start_urls

run 
===
scrapy crawl mobile_de # from scrapy-mobile_de directory

To automate put it in crontab:

*/2 * * * * cd scrapy-mobile_de && scrapy crawl --nolog mobile_de
