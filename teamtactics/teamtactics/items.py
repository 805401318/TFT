# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TeamtacticsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    health = scrapy.Field()
    mana_int = scrapy.Field()
    mana_max = scrapy.Field()
    ack = scrapy.Field()
    asp = scrapy.Field()
    ar = scrapy.Field()
    mr = scrapy.Field()
    ar_health = scrapy.Field()
    mr_health = scrapy.Field()
    vangurad = scrapy.Field()
    mystic_health = scrapy.Field()
    pass
