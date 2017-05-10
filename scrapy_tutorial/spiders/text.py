# -*- coding: utf-8 -*-
import scrapy


class TextSpider(scrapy.Spider):
    name = "text"
    allowed_domains = ["www.ramwin.com"]
    start_urls = ['http://www.ramwin.com/']

    def parse(self, response):
        pass
