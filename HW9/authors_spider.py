#and then run this script  ---- 
#scrapy runspider authors_spider.py -o authors_output.json

import scrapy
import json

class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        authors = []
        for author in response.css('div.quote small::text').getall():
            authors.append(author)

        formatted_data = self.convert_to_new_format(authors)
        self.save_data(formatted_data)

        self.log(f'Parsed {len(authors)} authors on {response.url}')

    def convert_to_new_format(self, authors):
        formatted_data = [{"author": author} for author in authors]
        return formatted_data

    def save_data(self, data):
        with open('authors_output.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        self.log(f'Saved {len(data)} authors to authors_output.json')
