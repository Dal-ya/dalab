db = {
    'user'     : 'root',
    'password' : 'password',
    'host'     : 'local',
    'port'     : 3306,
    'database' : 'test'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
JWT_SECRET_KEY = 'SECRET'
JWT_EXP_DELTA_SECONDS = 7 * 24 * 60 * 60
CODE = 'SECRET'