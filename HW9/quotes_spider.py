#scrapy runspider quotes_spider.py -o quotes_output.json

import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        quotes = []
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('small::text').get()
            tags = quote.css('div.tags a.tag::text').getall()

            quotes.append({
                'text': text,
                'author': author,
                'tags': tags,
            })

        formatted_data = self.convert_to_new_format(quotes)
        self.save_data(formatted_data)

        self.log(f'Parsed {len(quotes)} quotes on {response.url}')

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        else:
            self.log('No more pages to follow.')

    def convert_to_new_format(self, quotes):
        formatted_data = [
            {
                "tags": item["tags"],
                "author": item["author"],
                "quote": f'“{item["text"]}”'
            }
            for item in quotes
        ]
        return formatted_data

    def save_data(self, data):
        with open('quotes_output.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        self.log(f'Saved {len(data)} quotes to quotes_output.json')
