import bcrypt
import jwt

from functools import wraps

from flask import Flask, jsonify, request, current_app, Response, g
from flask.json import JSONEncoder
from sqlalchemy import create_engine, text
from datetime   import datetime, timedelta
from flask_cors import CORS

from news_catch import news_title_catch
from real_search import *


## 출처 : 깔끔한 파이썬 탄탄한 백엔드
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)


def get_user(user_id):
    user = current_app.database.execute(text("""
        SELECT
            id,
            name,
            created_at
        FROM users
        WHERE id = :user_id
    """), {
        'user_id' : user_id
    }).fetchone()

    return {
        'id' : user['id'],
        'name' : user['name'],
        'created_at' : user['created_at']
    } if user else None


def insert_user(user):
    return current_app.database.execute(text("""
        INSERT INTO users(
            name,
            hashed_password,
            code
        ) VALUES (
            :name,
            :password,
            :code
        )
    """), user).lastrowid


def get_user_id_and_password(name):
    row = current_app.database.execute(text("""
        SELECT 
            id,
            hashed_password
        FROM users
        WHERE name = :name
    """), {'name': name}).fetchone()

    return {
        'id': row['id'],
        'hashed_password': row['hashed_password']
    } if row else None


# Decorators
def login_required(f):      
    @wraps(f)                   
    def decorated_function(*args, **kwargs):
        access_token = request.headers.get('Authorization') 
        if access_token is not None:  
            try:
                payload = jwt.decode(access_token, current_app.config['JWT_SECRET_KEY'], 'HS256') 
            except jwt.InvalidTokenError:
                 payload = None     

            if payload is None: return Response(status=401)  

            user_id   = payload['user_id']  
            g.user_id = user_id
            g.user    = get_user(user_id) if user_id else None
        else:
            return Response(status = 401)  

        return f(*args, **kwargs)
    return decorated_function


def create_app(test_config = None):
    app = Flask(__name__)

    CORS(app)

    app.json_encoder = CustomJSONEncoder

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)
    
    database = create_engine(app.config['DB_URL'], encoding='utf-8', max_overflow=0)
    app.database = database


    @app.route('/sign-up', methods=['POST'])
    def sign_up():
        new_user = request.json
        if new_user['code'] == app.config['CODE']:
            new_user['password'] = bcrypt.hashpw(
                new_user['password'].encode('UTF-8'),
                bcrypt.gensalt()
            )

            new_user_id = insert_user(new_user)
            new_user = get_user(new_user_id)

            return jsonify(new_user)
        else:
            return 'WRONG', 401


    @app.route('/login', methods=['POST'])
    def login():
        credential = request.json
        name = credential['name']
        password = credential['password']
        user_credential = get_user_id_and_password(name)

        if user_credential and bcrypt.checkpw(password.encode('UTF-8'), user_credential['hashed_password'].encode('UTF-8')):
            user_id = user_credential['id']
            payload = {
                'user_id': user_id,
                'exp': datetime.utcnow() + timedelta(seconds = 60 * 60 * 24)
            }
            token = jwt.encode(payload, app.config['JWT_SECRET_KEY'], 'HS256') 

            return jsonify({        
                'access_token' : token.decode('UTF-8')
            })
        else:
            return '', 401


    @app.route('/')
    def home():
        return '환영합니다, /daum-news or /duam-rt, naver-rt (로그인 필요)로 이동해보세요!'


    @app.route('/daum-news', methods=['GET'])
    def duam_news_main():
        return '/daum-news/카테고리명 (사회, 정치, 경제, 문화, 국제, it)'


    @app.route('/daum-news/<category>', methods=['GET'])
    def daum_news(category):
        title  = news_title_catch(category)
        return jsonify(title)


    @app.route('/daum-rt', methods=['GET'])
    @login_required
    def daum_rt():
        daum_realtime = daum_realtime_search_crawling()
        # print(daum_realtime)
        return jsonify(daum_realtime)


    @app.route('/naver-rt', methods=['GET'])
    @login_required
    def naver_rt():
        naver_realtime = naver_realtime_search_crawling()
        # print(naver_realtime)
        return jsonify(naver_realtime)


    return app


if __name__=='__main__':
    app = create_app()
    app.run(host='0.0.0.0')