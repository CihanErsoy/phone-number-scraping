import scrapy
from scrapy.crawler import CrawlerProcess

class myFirstSpider(scrapy.Spider):

  name = "myFirstSpider"
  # start_requests method
  def start_requests(self):
    for x in range(1,5):
        urlx='https://ozeldersilan.com/ders_ara/ankara-matematik-ozel-ders?ozel_ders_sayfa='+str(x)
        url_list.append(urlx)
    for url in url_list:
        yield scrapy.Request(url = url,
                         callback = self.parse_front)
  # First parsing method
  def parse_front(self, response):
    course_blocks = response.xpath('//div[@class="col-lg-12 col-md-12 col-sm-12 col-xs-12"]/a/@href')
    links_to_follow = course_blocks.extract()
    for link in links_to_follow:
      yield response.follow(url = link,
                            callback = self.parse_pages)
  # Second parsing method
  def parse_pages(self, response):
    mail_adresi = response.xpath('//div[@class="row"]/div/div[2]/ul/li[3]/span/em/text()').extract()
    tel_no =response.xpath('//div[@class="row"]/div/div[2]/ul/li[2]/span/em/text()').extract()
    yield print(mail_adresi), print(tel_no)

url_list=list()
# Run the Spider
process = CrawlerProcess()
process.crawl(myFirstSpider)
process.start()        
