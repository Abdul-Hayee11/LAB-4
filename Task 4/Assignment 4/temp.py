
# Example 6
import scrapy

class UniversitySpider(scrapy.Spider):
    name = "university"
    start_urls = ["https://www.shanghairanking.com/rankings/arwu/2023"]

    def parse(self, response):
        for row in response.css('table tbody tr'):
            rank = row.css('.ranking::text').get()
            name = row.css('.univ-name::text').get()
            yield {"Rank": rank, "University": name}