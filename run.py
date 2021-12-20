from scrapy.crawler import CrawlerProcess

from spider import HLTVSpider

from config import USER_AGENT

process = CrawlerProcess(
    settings={"USER_AGENT": USER_AGENT, "FEEDS": {"out.json": {"format": "json"}, }, }
)

process.crawl(HLTVSpider)
process.start()
