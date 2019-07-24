import requests, json
from bs4 import BeautifulSoup
from enum import Enum


class Category(Enum):
    사회 = 'society'
    정치 = 'politics'
    경제 = 'economic'
    국제 = 'foreign'
    문화 = 'culture'
    it = 'digital'


def get_category_value(key):
    try:
        value = getattr(Category, key).value
        return value

    except AttributeError:
        print('잘못된 카테고리명이 입력되었습니다')
        return


def news_title_catch(*keys):
    title_dic = {}

    for key in keys:
        category_value = get_category_value(key)
        title_list = html_daum_news_crawling(category_value)
        title_dic['title'] = title_list
        # title_json = json.dumps(title_dic, ensure_ascii=False)
        # print(title_json)
        return title_dic


def html_daum_news_crawling(category_value):
    title_list = []

    url = 'https://media.daum.net/{0}/'.format(category_value)

    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    main_news_title_selector = '#cSub > div > div.section_cate.section_headline > div.item_mainnews.\#MCC\#cluster1 > div > strong > a'
    sub_news_title_selector = '#cSub > div > div.section_cate.section_headline > div.item_mainnews.\#MCC\#cluster1 > div > div > div > a'

    # news...list = [<a>text</a>]
    news_main_tag_list = soup.select(main_news_title_selector)
    news_sub_tag_list = soup.select(sub_news_title_selector)

    # [<a>text</a>] 에서 text 만 추출 후 출력
    for txt in news_main_tag_list:
        news_main_text = txt.text
        title_list.append(news_main_text)

    for txt in news_sub_tag_list:
        news_sub_text = txt.text
        title_list.append(news_sub_text)

    return title_list


