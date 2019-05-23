# 도움 받은 사이트
# 크롤링 : https://medium.com/@mjhans83/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%98%EA%B8%B0-908e78ee09e0
# 크롤링 : https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
# 파이썬 전반 : https://dojang.io/ (파이썬 코딩 도장)
# OrderedDict 관련: https://godoftyping.wordpress.com/2015/05/13/python-%EC%88%9C%EC%84%9C%EB%A5%BC-%EA%B8%B0%EC%96%B5%ED%95%98%EB%8A%94-%EC%82%AC%EC%A0%84%ED%98%95-ordereddict/

import collections
import requests
from bs4 import BeautifulSoup

# category 딕셔너리
# https://media.daum.net/{value}/ : all을 제외 모두 공통인 부분
category = {
    'all' : 'all',
    '사회' : 'society',
    '정치' : 'politics',
    '경제' : 'economic',
    '국제' : 'foreign',
    '문화' : 'culture',
    'it'  : 'digital',
}

# 위 category 딕녀너리가 순서대로 나올 수 있게 OrderedDict 사용
# 파이썬 3.7 부터는 OrderedDic 하지 않아도 순서대로 나온다고 함
ordered_category = collections.OrderedDict(category)

# 카테고리별 뉴스 타이틀 가져오기 함수 선언
def news_title_catch(*category): 
    # 매개변수 category의 type은 튜플이기 때문에 값 추출을 위해 반복문 사용
    for k in category:
        keyword = k

        # 전달인자가 'all' 인 경우
        if keyword == 'all' and keyword in ordered_category.keys():
            for key in ordered_category.keys():
                if key == 'all':
                    continue
                
                print('=== {0} ==='.format(key))

                value = ordered_category[key]
                html_daum_news_crawling(value)
        
        # 전달인자가 'all' 외 '사회', '경제' ... 이고 키에 해당하는 경우
        elif keyword in ordered_category.keys():
            print('=== {0} ==='.format(keyword))
            html_daum_news_crawling(ordered_category[keyword])
        
        # 전달인자가 category 딕셔너리 키에 없는 경우
        else:
            print('없는 카테고리 입니다')


# 다음 뉴스 크롤링 하기 함수 선언
def html_daum_news_crawling(category_value):
    # category 딕녀서리의 value를 공통되는 url 부분에 넣기
    url = 'https://media.daum.net/{0}/'.format(category_value)
    
    # 크롤링 할 사이트의 html 코드를 텍스트로 담고 파싱할 수 있게 설정
    html_text = requests.get(url).text
    soup      = BeautifulSoup(html_text, 'html.parser')

    # 크롤링 하고 싶은 다음 뉴스 타이틀의 셀렉터
    main_title_selector = '#cSub > div > div.section_cate.section_headline > div.item_mainnews.\#MCC\#cluster1 > div > strong > a'
    sub_title_selector  = '#cSub > div > div.section_cate.section_headline > div.item_mainnews.\#MCC\#cluster1 > div > div > div > a'

    # news = [<a ..>text</a>] 
    news_main = soup.select(main_title_selector)
    news_sub  = soup.select(sub_title_selector)
    
    # news_main = [<a ..>text</a>] 에서 text 만 추출 후 출력
    for txt in news_main:
        news_main_text = txt.text
        print(news_main_text)

    # news_sub = [<a ..>text</a>] 에서 text 만 추출 후 출력
    for txt in news_sub:
        news_sub_text = txt.text
        print(news_sub_text)


# 함수 호출, 실행해보기
news_title_catch('경제', 'it')

# news_title_catch('all')



'''
# 크롤링 test code

html_text = requests.get('https://media.daum.net/politics/').text
soup = BeautifulSoup(html_text, 'html.parser')

select = soup.select('#cSub > div > div.section_cate.section_headline > div.item_mainnews.\#MCC\#cluster1 > div > div > div > a')
print(select)

for txt in select:
    select_txt = txt.text
    print(select_txt)
'''