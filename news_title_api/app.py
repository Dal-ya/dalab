from flask import Flask, jsonify, request
from news_catch import news_title_catch


app = Flask(__name__)


@app.route('/daum-news', methods=['GET'])
def duam_news_main():
    return '/daum-news/카테고리명 (사회, 정치, 경제, 문화, 국제, it)'


@app.route('/daum-news/<category>', methods=['GET'])
def daum_news(category):
    title  = news_title_catch(category)
    return jsonify(title)