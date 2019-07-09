import requests
from bs4 import BeautifulSoup
from collections import OrderedDict


def daum_realtime_search_crawling():
    daum_rt_dic = {}
    
    html_daum = requests.get('https://daum.net').text
    soup = BeautifulSoup(html_daum, 'html.parser')
    select = soup.select('.hotissue_layer .txt_issue')

    tag_list = []
    for tag in select:
        tag_list.append(tag.text)

    # 크롤링 하면 키워드가 중복되어 하나를 제거해 주어야 한다. 
    # set 을 쓰면 순서가 바뀌기 때문에 OrderedDict 를 사용해야 한다.
    daum_rt_dic['daum_realtime'] = list(OrderedDict.fromkeys(tag_list))

    return daum_rt_dic


def naver_realtime_search_crawling():
    naver_rt_dic = {}

    html_naver = requests.get('https://www.naver.com/').text
    soup = BeautifulSoup(html_naver, 'html.parser')
    select = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k')

    tag_list = []
    for tag in select:
        tag_list.append(tag.text)
    
    naver_rt_dic['naver_realtime'] = list(OrderedDict.fromkeys(tag_list))
    
    return naver_rt_dic