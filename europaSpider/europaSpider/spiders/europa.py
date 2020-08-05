# -*- coding: utf-8 -*-
import scrapy
import re

from europaSpider.europaSpider.items import EuropaspiderItem


class EuropaSpider(scrapy.Spider):
    name = 'europa'
    # allowed_domains = ['ema.europa.eu']
    start_urls = [
        'https://www.ema.europa.eu/en/medicines/ema_group_types/ema_medicine/field_ema_web_categories%253Aname_field/Human']

    def parse(self, response):
        # 实例化管道
        item = EuropaspiderItem()

        # 得到页面1的所有url_part
        url_part_list = response.xpath('//div[@class="ecl-u-mt-s"]/ul/li/a/@href').getall()
        # 得到页面1所有需要内容（未正则）
        url_content_list = response.xpath(
            '//div[@class="ecl-u-mt-s"]/ul/li/a/div[@class="ecl-list-item__body"]').getall()

        # 调用parse.re函数，得到第一页需要内容的列表
        medicine_name_list = self.parse_re(url_content_list)[0]
        indication_list = self.parse_re(url_content_list)[1]
        authorization_date_list = self.parse_re(url_content_list)[2]
        update_date_list = self.parse_re(url_content_list)[3]
        revision_times_list = self.parse_re(url_content_list)[4]

        print('^^^^^^^^^^^^^^^', revision_times_list, len(revision_times_list))
        for url_part in url_part_list:
            # 拼接完整的url
            url = response.urljoin(url_part)
            yield scrapy.Request(url, callback=self.parse_page2)

    # 定义正则处理的函数
    def parse_re(self, url_content_list):
        medicine_name_list, indication_list, authorization_date_list, update_date_list, revision_times_list = [], [], [], [], []
        for url_content in url_content_list:
            # 匹配单个数据的指定内容
            medicine_name = re.search(':\\n(.*?)<', url_content).group(1).strip()
            indication = re.search('<small>\\n(.*?)<', url_content).group(1).replace(' ', '')
            authorization_date = re.search('<br>Date of authorisation:(.*?),', url_content).group(1).strip()
            update_date = re.search('Last updated:(.*?)<', url_content).group(1).strip()
            revision_times = re.search('Revision:(.*?),', url_content).group(1).strip()
            # 把指定内容存在指定列表中
            medicine_name_list.append(medicine_name)
            indication_list.append(indication)
            authorization_date_list.append(authorization_date)
            update_date_list.append(update_date)
            revision_times_list.append(revision_times)
        return medicine_name_list, indication_list, authorization_date_list, update_date_list, revision_times_list

    def parse_page2(self, response):
        pass

    def start_requests(self):
        post_url = 'https://www.ema.europa.eu/en/views/ajax'
        formdata = {
            
        }


