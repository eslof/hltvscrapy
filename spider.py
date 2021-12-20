import itertools

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst

from config import *
from item import HLTVItem

# number of pages to scrape
PAGE_COUNT = 2


class HLTVSpider(scrapy.Spider):
    """ Lite scraping of HLTV result history for CS:GO matches. """
    name = "hltvspider"
    allowed_domains = [DOMAIN]
    match_type = "Lan"  # or "Online" to scrape online matches
    header = {"USER_AGENT": USER_AGENT}

    def start_requests(self):
        last_url = BASE_CRAWL_URL
        for i in range(PAGE_COUNT):
            # omitting offset query if it's 0
            url = CRAWL_URL % (
                (OFFSET_QUERY % (1 + i)) if i > 0 else "",
                self.match_type,
            )
            self.header["Referer"] = last_url  # natural referral
            last_url = url
            yield Request(url=url, headers=self.header, callback=self.parse)

    def parse(self, resp):
        matches = (
            match for match in (day.css(MATCH_SELECTOR) for day in resp.css(DAY_SELECTOR))
        )
        for match in itertools.chain(*matches):
            loader = ItemLoader(item=HLTVItem(), selector=match)
            loader.default_output_processor = TakeFirst()
            loader.add_value("match_type", self.match_type)
            loader.add_css("timestamp", "::attr(data-zonedgrouping-entry-unix)")
            loader.add_css("url_path", "a::attr(href)")
            loader.add_css("team_1", 'div[class="line-align team1"] ::text')
            loader.add_css("team_1_score", "td[class=result-score]")
            loader.add_css("team_2", 'div[class="line-align team2"] ::text')
            loader.add_css("team_2_score", "td[class=result-score]")
            yield loader.load_item()
