# 도움 받은 사이트
# https://medium.com/@mjhans83/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%98%EA%B8%B0-908e78ee09e0
# https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
# 파이썬 코딩 도장 : https://dojang.io/

import requests
from bs4 import BeautifulSoup

# 다음 뉴스 크롤링 하기
def html_daum_news(url):
    # 크롤링 할 사이트의 html 코드를 텍스트로 담고 파싱할 수 있게 설정(?)
    html_text = requests.get(url).text
    soup      = BeautifulSoup(html_text, 'html.parser')

    # 크롤링 하고 싶은 다음 뉴스 타이틀의 셀렉터
    main_title_selector = '#cSub > div > div.section_cate.section_headline > div.item_mainnews.\#MCC\#cluster1 > div > strong > a'
    sub_title_selector  = '#cSub > div > div.section_cate.section_headline > div.item_mainnews.\#MCC\#cluster1 > div > div > div > a'

    if url == 'https://media.daum.net/society/':
        # society_news = [<a ..>text</a>] 
        society_news_main = soup.select(main_title_selector)
        society_news_sub  = soup.select(sub_title_selector)
        
        # society_news_main = [<a ..>text</a>] 에서 text 만 추출 후 출력
        for txt in society_news_main:
            society_news_main_text = txt.text
            print(society_news_main_text)
    
        # society_news_sub = [<a ..>text</a>] 에서 text 만 추출 후 출력
        for txt in society_news_sub:
            society_news_sub_text = txt.text
            print(society_news_sub_text)

    elif url == 'https://media.daum.net/politics/':
        # politics_news = [<a ..>text</a>]
        politics_news_main = soup.select(main_title_selector)
        politics_news_sub  = soup.select(sub_title_selector)

        # politics_news_main = [<a ..>text</a>] 에서 text 만 추출 후 출력
        for txt in politics_news_main:
            politics_news_main_text = txt.text
            print(politics_news_main_text)

        # politics_news_sub = [<a ..>text</a>] 에서 text 만 추출 후 출력
        for txt in politics_news_sub:
            politics_news_sub_text = txt.text
            print(politics_news_sub_text)    

    elif url == 'https://media.daum.net/economic/':
        # economic_news = [<a ..>text</a>]
        economic_news_main = soup.select(main_title_selector)
        economic_news_sub  = soup.select(sub_title_selector)

        # economic_news_main = [<a ..>text</a>] 에서 text 만 추출 후 출력
        for txt in economic_news_main:
            economic_news_main_text = txt.text
            print(economic_news_main_text)
        
        # economic_news_sub = [<a ..>text</a>] 에서 text 만 추출 후 출력
        for txt in economic_news_sub:
            economic_news_sub_text = txt.text
            print(economic_news_sub_text)

    elif url == 'https://media.daum.net/foreign/':
        # foreign_news = [<a ..>text</a>]
        foreign_news_main = soup.select(main_title_selector)
        foreign_news_sub  = soup.select(sub_title_selector)

        # foreign_news_main = [<a ..>text</a>] 에서 text 만 추출 후 출력
        for txt in foreign_news_main:
            foreign_news_main_text = txt.text
            print(foreign_news_main_text)

        # foreign_news_sub = [<a ..>text</a>]에서 text 만 추출 후 출력
        for txt in foreign_news_sub:
            foreign_news_sub_text = txt.text
            print(foreign_news_sub_text)

    elif url == 'https://media.daum.net/culture/':
        # culture_news = [<a ..>text</a>]
        culture_news_main = soup.select(main_title_selector)
        culture_news_sub  = soup.select(sub_title_selector)

        # culture_news_main = [<a ..>text</a>] 에서 text 만 추출 후 출력
        for txt in culture_news_main:
            culture_news_main_text = txt.text
            print(culture_news_main_text)
        
        # culture_news_sub = [<a ..>text</a>] 에서 text 만 추출 후 출력
        for txt in culture_news_sub:
            culture_news_sub_text = txt.text
            print(culture_news_sub_text)

    elif url == 'https://media.daum.net/digital/':
        # digital_news = [<a ..>text</a>]
        digital_news_main = soup.select(main_title_selector)
        digital_news_sub  = soup.select(sub_title_selector)

        # culture_news_main = [<a ..>text</a>] 에서 text 만 추출 후 출력
        for txt in digital_news_main:
            digital_news_main_text = txt.text
            print(digital_news_main_text)
        
        # culture_news_sub = [<a ..>text</a>] 에서 text 만 추출 후 출력
        for txt in digital_news_sub:
            digital_news_sub_text = txt.text
            print(digital_news_sub_text)

    else:
        print('확인할 수 없는 url 입니다')


# 카테고리 별 뉴스 타이틀 가져오기
def news_title_catch(*categories):  # 파이썬 언패킹 https://dojang.io/mod/page/view.php?id=2345 
    for category in categories:
        if category == '사회':
            print('=== 사회 ===')
            html_daum_news('https://media.daum.net/society/')
        
        elif category == '정치':
            print('=== 정치 ===')
            html_daum_news('https://media.daum.net/politics/')

        elif category == '경제':
            print('=== 경제 ===')
            html_daum_news('https://media.daum.net/economic/')

        elif category == '국제':
            print('=== 국제 ===')
            html_daum_news('https://media.daum.net/foreign/')

        elif category == '문화':
            print('=== 문화 ===')
            html_daum_news('https://media.daum.net/culture/')

        elif category == 'it':
            print('=== it ===')
            html_daum_news('https://media.daum.net/digital/')

        else:
            print('사회, 정치, 경제, 국제, 문화, it 중 입력해주세요 모두 보려면 *all_category' )   


all_category = ['사회', '정치', '경제', '국제', '문화', 'it']

news_title_catch('사회', 'it')

# news_catch(*all_category)



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