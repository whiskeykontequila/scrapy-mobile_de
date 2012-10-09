# Scrapy settings for mobile_de project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'mobile_de'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['mobile_de.spiders']
NEWSPIDER_MODULE = 'mobile_de.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

