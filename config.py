DOMAIN = "hltv.org"
BASE_URL = "https://www." + DOMAIN
RESULTS_PATH = "/results"
BASE_CRAWL_URL = BASE_URL + RESULTS_PATH
MATCHTYPE_QUERY = "matchType=%s"
CRAWL_URL = BASE_CRAWL_URL + "?%s" + MATCHTYPE_QUERY
OFFSET_QUERY = "offset=%d&"
PAGE_OFFSET = 100
DAY_SELECTOR = "div[class=results-all] > div[class=results-sublist]"
MATCH_SELECTOR = 'div[class="result-con "]'
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
