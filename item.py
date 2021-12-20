from functools import partial

import scrapy
from itemloaders.processors import MapCompose
from w3lib.html import remove_tags


def clean_name(value):
    """ Remove newlines and strip spaces from team name. """
    return ''.join(value).replace('\n', '').strip()


def clean_url(value):
    """ Remove prefix from url. """
    return value[len('/matches'):]


def get_score(team_number, value):
    """ Split score for given team.

     :param team_number: e.g. 1 or 2
     """
    return value.split()[0] if team_number == 1 else value.split()[2]


class HLTVItem(scrapy.Item):
    """ The results of a match series between two CS:GO teams. """
    timestamp = scrapy.Field(input_processor=MapCompose(int))
    match_type = scrapy.Field()
    url_path = scrapy.Field(input_processor=MapCompose(clean_url))
    team_1 = scrapy.Field(input_processor=clean_name)
    team_1_score = scrapy.Field(
        input_processor=MapCompose(remove_tags, partial(get_score, 1), int)
    )
    team_2 = scrapy.Field(input_processor=clean_name)
    team_2_score = scrapy.Field(
        input_processor=MapCompose(remove_tags, partial(get_score, 2), int)
    )
