# -*- coding: utf-8 -*-
import scrapy
from .. import items


class TextSpider(scrapy.Spider):
    name = "text"
    allowed_domains = ["www.ramwin.com"]
    start_urls = ['http://www.ramwin.com/testrest/text/', 'http://www.ramwin.com/testrest/text/?secret=3']

    def parse(self, response):
        # self.logger.info("A response from %s just arrived!", response.url)
        self.logger.warning("A response from %s just arrived!", response.url)
        for li in response.xpath('//li'):
            # yield {
            #     "text": li.xpath('.//text()').extract_first(),
            #     "id": li.css('li::attr(title)').extract_first(),
            # }
            item = items.ScrapyTutorialItem(
                text=li.xpath('.//text()').extract_first(),
                id=li.css('li::attr(title)').extract_first()
            )
            yield item
        if response.xpath('//a'):
            # 生成一个新的请求队列
            yield scrapy.Request(response.xpath('//a/@href').extract_first(), callback=self.parse)
        pass
