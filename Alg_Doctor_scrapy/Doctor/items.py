# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoctorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DoctorProfileItem(scrapy.Item):
    name=scrapy.Field()
    specialty=scrapy.Field()
    address=scrapy.Field()
    working_hours=scrapy.Field()
    contact=scrapy.Field()