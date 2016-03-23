# -*- coding:utf-8 -*-
import scrapy
from weibo.items import WeiboItem

class WeiboSpider(scrapy.Spider):
    name = 'weibo'

    def start_requests(self):
        cookies = {'_T_WM': '40c5a1b42ccafae3f8cee147a4f1351d', 
                'SUHB': '0ftoM79MqQ_Iof', 
                'H5_INDEX': '0_all', 
                'H5_INDEX_TITLE':u'No7小强', 
                'SUB': '_2A2579Y0UDeRxGeRK4lES9S7PyTuIHXVZGRNcrDV6PUJbrdBeLRTjkW1LHes1rjZm75tojmUOF5u-Znm33zBMoQ..',
                'SSOLoginState': '1458699588', 
                'M_WEIBOCN_PARAMS': 'uicode=20000174', 
                'gsid_CTandWM': '4uymCpOz5J13JhgPYKnu8asDk5h'}
        for i in range(1, 190):
            res = scrapy.Request('http://weibo.cn/?since_id=0&max_id=DmHmv2T3c&page=%d' % i, cookies = cookies, callback = self.after_login)
            yield res

    def after_login(self, response):
        alls = response.xpath('//div[starts-with(@id, "M_")]')
        print '-----------------------'
        print alls
        print '~~~~~~~~~~~~~~~~~~~~~~'
        for each in alls:
            item = WeiboItem()
            item['author'] =each.xpath('div/a[@class="nk"]/text()').extract()[0]
            cont = each.xpath('div/span[@class="ctt"]')
            item['content'] = cont.xpath('string(.)').extract()
            item['time'] =each.xpath('div/span[@class="ct"]/text()').extract()[0]
            print item['author']
            yield item

