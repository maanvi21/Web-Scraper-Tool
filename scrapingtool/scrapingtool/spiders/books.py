import scrapy
from pathlib import Path

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/category/books/mystery_3/index.html", "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"]

    def parse(self, response):
        page=response.url.split("/")[2]
        pass
