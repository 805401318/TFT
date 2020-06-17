import scrapy
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider
from teamtactics.teamtactics.items import TeamtacticsItem
from scrapy import Request

class Spider(CrawlSpider):
    name = "spider"

    def start_requests(self):
        urls = [
            'https://leagueoflegends.fandom.com/wiki/List_of_champions_(Teamfight_Tactics)',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        pages = response.xpath('//span[@style="white-space:normal"]/a/@src')
        for page in pages:
            page_url=page.extractfirst()
            yield Request(url=page_url,callback=self.parse)

    def parse(self, response):
        i = ItemLoader(item=TeamtacticsItem(), response=response)
        i.add_xpath('name', '//h2[@data-source="championname"][1]/text()')
        i.add_xpath('health', '//div[@class="pi-data-value pi-fon"][1]/text()',re='')
        i.add_xpath('mana_int', '//h2[@class="championname"][1]/text()')
        i.add_xpath('mana_max', '//h2[@data-source="championname"][1]/text()')
        i.add_xpath('ack', '//h2[@data-source="championname"][1]/text()')
        i.add_xpath('asp', '//h2[@data-source="championname"][1]/text()')
        i.add_xpath('ar', '//h2[@data-source="championname"][1]/text()')
        i.add_xpath('mr', '//h2[@class="championname"][1]/text()')
        i.add_xpath('ar_health', '//h2[@class="championname"][1]/text()')
        i.add_xpath('mr_health', '//h2[@class="championname"][1]/text()')
        i.add_xpath('vanguard', '//h2[@class="championname"][1]/text()')
        i.add_xpath('crawler', '//h2[@class="championname"][1]/text()')
