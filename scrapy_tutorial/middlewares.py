# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import scrapy
import logging
import time


class MyMiddleWare(object):

    def process_spider_exception(self, response, exception, spider):
        # 这个报错是尝试多次，一直失败。然后重新尝试的
        logging.error("报错了哦")
        logging.error("报错日志, process_spider_exception")
        # import ipdb
        # ipdb.set_trace()
        if hasattr(spider, 'secret_key') == False:
            spider.secret_key = 1
        else:
            spider.secret_key += 1
        if spider.secret_key >= 4:
            return [
                {'id': None, "text": None}
            ]
        else:
            time.sleep(spider.secret_key * 2)
            yield scrapy.Request(response.url+"&secret=%d" % spider.secret_key, callback=spider.parse)



class ScrapyTutorialSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
