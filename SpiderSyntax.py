import scrapy
from scrapy.crawler import CrawlerProcess

class Spider_Name(scrapy.Spider):

    name = 'Spider Name'

    def start_requests(self):
        url = 'site url'
        yield scrapy.Request(url = url, callback= self.parse1)

    def parse1(self, response):
        ## Code to parse
        yield response.follow(url = 'url', callback= self.parse2)

    def parse2(self, response):
        ## Code to parse

process = CrawlerProcess()
process.crawl(Spider_Name)
process.start()
