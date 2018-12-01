# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei


from fake_useragent import UserAgent
us = UserAgent()
print(us.random)


在pipeline中定义一个类 ，用来将数据存入数据库：
    from .settings import *

    class DaoPipeline(object):

        def __init__(self):
            host = MONGODB_HOST
            port = MONGIDB_PORT
            dbNAME = MONGODB_DBNAME
            conn = pymongo.MongoClient(host=host, port=port)
            db = conn[dbNAME]
            self.myset = db[dbNAME]

        def process_item(seld, item, spider):
            bookInfo = dict(item)
            self.myset.insert(bookInfo)
            print("存入数据库成功")
            return item


scrapy 工作流：
    1、Engine 首先打开一个网站，找到处理该网站的Spider，并向该Spider请求第一个要爬取的URL
    2、Engine 从SPider中获取到第一个要爬取的URL，并通过Sceduler以Request的形式调度。
    3、Engine 向Scheduler请求下一个要爬取的URL
    4、Sceduler 返回下一个要爬取的URL给Engine, Engine将URL通过Downloader Middlewares转发给
    Downloader下载，
    5、一旦页面下载完成，Downloader生成该页面的Response, 并将其通过Downloader Middlewares 发送
    给Engine。
    6、engine从下载器中接受到response，并将其通过spider Middlewares发送给spider处理
    7、spider处理response，并将爬取到的item及新的request给engine
    8、engine将spider返回给item给itempipline 将新的request给scheduler
    9、重复第2步到第8步，直到scheduler中没有更多的request，engine关闭网站，爬取结束

    import copy
    deep.deep.copy()
