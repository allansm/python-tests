import scrapy
import logging
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request

class test(scrapy.Spider):
    name = 'test'
    
    custom_settings = {
        "MEDIA_ALLOW_REDIRECTS": True
    }
    
    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        
        for url in self.start_urls:
            yield Request(url, headers=headers)
    
    def parse(self, resp):
        print(resp.text)


logging.getLogger('scrapy').setLevel(logging.WARNING)
logging.getLogger('scrapy').propagate = False

process = CrawlerProcess()
process.crawl(test, start_urls=[input("url:")])
process.start()
