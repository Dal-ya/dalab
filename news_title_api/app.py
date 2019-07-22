from flask import Flask, jsonify, request
from news_catch import news_title_catch
from real_search import *
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    return '환영합니다, /daum-news 로 이동해보세요!'


@app.route('/daum-news', methods=['GET'])
def duam_news_main():
    return '/daum-news/카테고리명 (사회, 정치, 경제, 문화, 국제, it)'


@app.route('/daum-news/<category>', methods=['GET'])
def daum_news(category):
    title  = news_title_catch(category)
    return jsonify(title)


@app.route('/daum-rt', methods=['GET'])
def daum_rt():
    daum_realtime = daum_realtime_search_crawling()
    print(daum_realtime)
    return jsonify(daum_realtime)


@app.route('/naver-rt', methods=['GET'])
def naver_rt():
    naver_realtime = naver_realtime_search_crawling()
    print(naver_realtime)
    return jsonify(naver_realtime)



app.run(host='0.0.0.0')