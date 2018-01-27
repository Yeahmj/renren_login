# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']

    # 模拟登陆需要重写
    def start_requests(self):
        url = self.start_urls[0]
        post_data = {
            'email':'17173805860',
            'password':'1qaz@WSX3edc',
        }

        # 发送post请求
        yield scrapy.FormRequest(
            url,
            formdata=post_data
        )

    def parse(self, response):
        with open('renren.html', 'wb') as f:
            f.write(response.body)

