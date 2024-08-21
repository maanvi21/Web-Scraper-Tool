from typing import Iterable
import scrapy
from pathlib import Path

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = [
          " https://toscrape.com"
        ]
    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",  
            "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html" 
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # self.log(f"Processing URL: {response.url}")
        page = response.url.split("/")[-2]
        filename = f"books-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
