# -*- coding: utf-8 -*-
import scrapy


class RenrenFormSpider(scrapy.Spider):
    name = 'renren_form'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def parse(self, response):
        post_data = {
            'email': '17173805860',
            'password': '1qaz@WSX3edc',
        }

        # 调用FormRequest的类方法，模拟登陆
        yield scrapy.FormRequest.from_response(
            response,
            formdata=post_data,
            callback=self.parse_login
        )

    def parse_login(self, response):
        with open('renren2.html','wb') as f:
            f.write(response.body)
