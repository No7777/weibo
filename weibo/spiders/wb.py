# -*- coding:utf-8 -*-
import scrapy
from weibo.items import WeiboItem

class WeiboSpider(scrapy.Spider):
    name = 'weibo'

    def start_requests(self):
        cookies = {'H5_INDEX': '0_all',
                'H5_INDEX_TITLE': u'No7小强',
                '_T_WM': '40c5a1b42ccafae3f8cee147a4f1351d',
                'SUHB': '0WGdI9a3ifKtsU', 
                'SUB':'_2A256AAQIDeRxGeRK4lES9S7PyTuIHXVZCqxArDV6PUJbrdBeLXDukW1LHes0Lk9Lh1I64koiNLtkt2ZRcKT3lw..',
                'M_WEIBOCN_PARAMS': 'uicode=20000061&featurecode=20000180&fid=3961273848699162&oid=3961273848699162', 
                'gsid_CTandWM': '4ujoCpOz5tuu5PIvhDEddasDk5h'}
        for i in range(1, 10):
            res = scrapy.Request('http://weibo.com/' , cookies = cookies, callback = self.after_login)
            print res.body
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

