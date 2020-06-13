import scrapy


class Spider(scrapy.Spider):
    name = "spider"

    def start_requests(self):
        urls = [
            'https://leagueoflegends.fandom.com/wiki/List_of_champions_(Teamfight_Tactics)',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)