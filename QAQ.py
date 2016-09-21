# !/usr/bin/env python
# encoding=utf-8

import scrapy
import re
from scrapy import Selector
from scrapy.crawler import CrawlerProcess
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError


class LittleSpider(scrapy.Spider):
    name = "QwQSpider"

    def start_requests(self):
        for u in range(23411, 1, -1):
            url = "https://h.nimingban.com/f/%E7%BB%BC%E5%90%88%E7%89%881?page=" + str(u)
            yield scrapy.Request(url, callback=self.parse_httpbin,
                                 errback=self.errback_httpbin,
                                 dont_filter=True)

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

    def parse_httpbin(self, response):
        _filename = "G:\spider.txt"
        with open(_filename, 'a', encoding='utf-8') as f:
            _list = Selector(response=response)\
                .xpath("//div[@class='h-threads-content']")\
                .re("<d.*>\s*([\S\s]*?)\s*</div")
            for i in _list:
                _str = re.sub(r'<fo.*?nt>', '', i.replace('<br>', ''))
                if len(_str) > 0:
                    f.write(_str + '\n')
        # with open("spider.html", 'wb') as f:
        #    f.write(response.body)

if __name__ == '__main__':
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(LittleSpider)
    process.start()
