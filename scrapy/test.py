import scrapy
from scrapy.crawler import CrawlerProcess
import logging

class test(scrapy.Spider):
    name = 'test'
    start_urls = [input("url:")]
              
    def parse(self, resp):
        for n in resp.css("a::attr(href)").extract():
            yield{
                "link":n,
            }
            
            print(n)

logging.getLogger('scrapy').setLevel(logging.WARNING)
logging.getLogger('scrapy').propagate = False

process = CrawlerProcess()
process.crawl(test)
process.start()
