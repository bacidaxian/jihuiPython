# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EuropaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    medicine_name = scrapy.Field()
    indication = scrapy.Field()
    authorization_date = scrapy.Field()
    update_date = scrapy.Field()
    revision_times = scrapy.Field()
    application_type = scrapy.Field()
    overview_content = scrapy.Field()
    overview_pdf = scrapy.Field()
    aut_prod_dtl = scrapy.Field()
    aut_pub_dtl = scrapy.Field()
    prod_info_pdf = scrapy.Field()
    assessment_title_1 = scrapy.Field()
    assessment_pdf_1 = scrapy.Field()
    assessment_title_2 = scrapy.Field()
    assessment_pdf_2 = scrapy.Field()
