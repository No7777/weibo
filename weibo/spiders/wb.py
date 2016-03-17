# -*- coding:utf-8 -*-
import scrapy
from weibo.items import WeiboItem

class WeiboSpider(scrapy.Spider):
    name = 'weibo'

    def start_requests(self):
        cookies = {'M_WEIBOCN_PARAMS': 'from=home&luicode=20000174', 'SUB': '_2A2577k3eDeRxGeRK4lES9S7PyTuIHXVZEVOWrDV6PUJbrdANLUzDkW1LHesFvPNBrnupLGYvCjmQgtObRLy65A..', 'SUHB': '09P89Q5jirKsV1', '_T_WM': '40c5a1b42ccafae3f8cee147a4f1351d', 'gsid_CTandWM': '4ulUbd311DUmGGa4QTj3GasDk5h'}
        return [scrapy.Request('http://weibo.cn/?since_id=DmF9bhji0&max_id=DmEWM7xoj&page=1', cookies = cookies, callback = self.after_login)]

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
            print item['content']
            print item['time']
        yield item

