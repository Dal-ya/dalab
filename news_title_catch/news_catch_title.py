# 도움 받은 사이트
# 크롤링 : https://medium.com/@mjhans83/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%98%EA%B8%B0-908e78ee09e0
# 크롤링 : https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
# 파이썬 전반 : https://dojang.io/ (파이썬 코딩 도장)
# OrderedDict 관련: https://godoftyping.wordpress.com/2015/05/13/python-%EC%88%9C%EC%84%9C%EB%A5%BC-%EA%B8%B0%EC%96%B5%ED%95%98%EB%8A%94-%EC%82%AC%EC%A0%84%ED%98%95-ordereddict/
# enum :
# https://docs.python.org/3.4/library/enum.html
# https://pythonkim.tistory.com/90
# https://stackoverflow.com/questions/12801912/python-3-x-java-valueof-equivalent-in-python-3-x
# 예외처리 : https://wayhome25.github.io/python/2017/02/26/py-12-exception/

import requests
from bs4 import BeautifulSoup
from enum import Enum


def digital():
    url = 'https://media.daum.net/digital'
    html_daum_news_crawling(url)


category = {
    'all': 'all',
    '사회': 'society',
    '정치': 'politics',
    '경제': 'economic',
    '국제': 'foreign',
    '문화': 'culture',
    'it': 'digital',
}

key = 'it'
category[key]()



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
        print('===={0}===='.format(key))
        return value

    except AttributeError:
        print('잘못된 이름입니다')
        return


def news_title_catch(*keys):
    for key in keys:
        if key == 'all':
            category_keys_list = list(Category.__members__.keys())
            news_title_catch(*category_keys_list)
            return

        category_value = get_category_value(key)

        html_daum_news_crawling(category_value)


def html_daum_news_crawling(category_value):
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
        print(news_main_text)

    for txt in news_sub_tag_list:
        news_sub_text = txt.text
        print(news_sub_text)


# news_title_catch('경제', 'it')
news_title_catch('all')
# news_title_catch('정치')



'''
# 크롤링 예제 code
html_text = requests.get('https://media.daum.net/politics/').text
soup = BeautifulSoup(html_text, 'html.parser')
select = soup.select('#cSub > div > div.section_cate.section_headline > div.item_mainnews.\#MCC\#cluster1 > div > div > div > a')
print(select)
for txt in select:
    select_txt = txt.text
    print(select_txt)
'''
