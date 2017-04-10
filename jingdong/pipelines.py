# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymongo import MongoClient

class JingdongPipeline(object):
    # def __init__(self):
    #     self.client = MongoClient()
    #     self.database = self.client['jingdong']
    #     self.db = self.database['jingdong_infomation']
    #
    # def process_item(self, item, spider):#这里以每个用户url_token为ID，有则更新，没有则插入
    #     self.db.update({'goods_id':item['goods_id']},dict(item),True)
    #     return item
    #
    # def close_spider(self,spider):
    #     self.client.close()






    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',port=3306,user ='root',passwd='root',db='jingdong',charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:#有些标题会重复，所以添加异常
            title = item['title']
            comment_count = item['comment_count']  # 评论数
            shop_url = item['shop_url'] # 店铺链接
            price = item['price']
            goods_url = item['goods_url']
            shops_id = item['shops_id']
            goods_id =int(item['goods_id'])
            #sql = 'insert into jingdong_goods(title,comment_count,shop_url,price,goods_url,shops_id) VALUES (%(title)s,%(comment_count)s,%(shop_url)s,%(price)s,%(goods_url)s,%(shops_id)s,)'
            try:
                self.cursor.execute("insert into jingdong_goods(title,comment_count,shop_url,price,goods_url,shops_id,goods_id)values(%s,%s,%s,%s,%s,%s,%s)", (title,comment_count,shop_url,price,goods_url,shops_id,goods_id))

                self.conn.commit()
            except Exception as e:
                pass

        except Exception as e:
            pass

    # def close_spider(self):
    #     self.conn.close()