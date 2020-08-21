import scrapy
from scrapy.crawler import CrawlerProcess

class UC_Spider(scrapy.Spider):

    name = 'UC spider'

    def start_requests(self):
        url = 'https://www.universitecentrale.net/fr/12/diplomes-d-ingenieur'
        yield scrapy.Request(url = url, callback= self.parse1)

    def parse1(self, response):
        diploma_names = response.xpath('//div[@class="diploma"]/a/text()').extract()
        diploma_urls = response.xpath('//div[@class="diploma"]/a/@href').extract()
        print(diploma_names)
        print(diploma_urls)
        L1 = diploma_names
        L2 = diploma_urls
        ##UC_dict = dict(zip(diploma_names,diploma_urls))

        ##for url in diploma_urls:
        ##    yield response.follow(url = 'url', callback= self.parse2)



L1= []
L2= []

process = CrawlerProcess()
process.crawl(UC_Spider)
process.start()

print(L1)
print(L2)



