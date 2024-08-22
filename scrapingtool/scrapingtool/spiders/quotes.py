import scrapy
import json

class QuotesSpiderSpider(scrapy.Spider):
    name = "quotes_spider"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/tag/humor/"]

    def parse(self, response):
        quotes = response.css('div.quote')
        results = []
        for quote in quotes:
            item = {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
            results.append(item)
        
        self.write_to_json(results)

    def write_to_json(self, data):
        with open('quotes.json', 'w') as f:
            json.dump(data, f, indent=4)