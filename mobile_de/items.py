# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class MobileDeItem(Item):
    # define the fields for your item here like:
    # name = Field()
    id = Field()
    listEntryTitle = Field()
    URL = Field()
    vehicleLocation = Field()
    pricePrimaryCountryOfSale = Field()
    mileage = Field()
    firstRegistration = Field()
    vendorType = Field()
#    pass
