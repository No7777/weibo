# -*- coding:utf-8 -*-
import scrapy
from weibo.items import WeiboItem
import json

class WeiboSpider(scrapy.Spider):
    name = 'weibo2'

    def start_requests(self):
        cookies = {'_T_WM': '40c5a1b42ccafae3f8cee147a4f1351d', 
                'SUHB': '0ftoM79MqQ_Iof', 
                'H5_INDEX': '0_all', 
                'H5_INDEX_TITLE':u'No7小强', 
                'SUB': '_2A2579Y0UDeRxGeRK4lES9S7PyTuIHXVZGRNcrDV6PUJbrdBeLRTjkW1LHes1rjZm75tojmUOF5u-Znm33zBMoQ..',
                'SSOLoginState': '1458699588', 
                'M_WEIBOCN_PARAMS': 'uicode=20000174', 
                'gsid_CTandWM': '4uymCpOz5J13JhgPYKnu8asDk5h'}

        res = scrapy.Request('http://m.weibo.cn/', cookies = cookies, callback = self.after_login)
        yield res

    def after_login(self, response):
        for i in range(186):
            yield scrapy.Request('http://m.weibo.cn/index/feed?format=cards&next_cursor=3956134912238794&page=%d' % (i+1), self.home)

    def home(Self, response):
        item = WeiboItem()
        objs = json.loads(response.body)
        obj = objs[0]
        for o in obj['card_group']:
            item['content'] = o['mblog']['text']
            item['author'] = o['mblog']['user']['screen_name']
            yield item
