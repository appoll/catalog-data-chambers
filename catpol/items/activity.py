import scrapy


class ActivityItem(scrapy.Item):
    name = scrapy.Field()
    dictionary = scrapy.Field()
    url = scrapy.Field()
