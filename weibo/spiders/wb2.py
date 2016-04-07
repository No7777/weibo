# -*- coding:utf-8 -*-
import scrapy
from weibo.items import WeiboItem
import json

class WeiboSpider(scrapy.Spider):
    name = 'weibo2'

    def start_requests(self):
        cookies = {
                'SSOLoginState': '1459927749',
                '_T_WM': '40c5a1b42ccafae3f8cee147a4f1351d',
                'SUHB': '08JKhOK2Y_ifT-', 
                'SUB':'_2A256AMqUDeRxGeRN71EQ9yrJyz-IHXVZCtbcrDV6PUJbrdBeLRHkkW1LHetutsd5wfvsSsscD3DRUQiI3A3XNA..',
                'M_WEIBOCN_PARAMS': 'uicode=20000174',
                'H5_INDEX': '0_all', 
                'H5_INDEX_TITLE':u'No7小强',  
                'gsid_CTandWM': '4uW6CpOz5C4E7zdTF9nJ19Pz887'}

        res = scrapy.Request('http://m.weibo.cn/', cookies = cookies, callback = self.after_login)
        yield res

    def after_login(self, response):
        for i in range(1):
            con = scrapy.Request('http://m.weibo.cn/page/pageJson?containerid=&containerid=102803&v_p=11&ext=&fid=102803&uicode=10000011&&page=%d' % (i+1), self.home)
            yield con

    def home(Self, response):
        item = WeiboItem()
        objs = json.loads(response.body)
        print objs
        #obj = objs[0]
        #for o in obj['card_group']:
            #item['content'] = o['mblog']['text']
            #item['author'] = o['mblog']['user']['screen_name']
            #yield item
