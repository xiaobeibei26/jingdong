# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    comment_count=scrapy.Field()#评论数
    shop_url =scrapy.Field()#店铺链接
    price =scrapy.Field()
    goods_url = scrapy.Field()
    shops_id = scrapy.Field()
    goods_id = scrapy.Field()#商品ID
