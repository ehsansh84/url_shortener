
MONGO_URL = 'mongodb://localhost:27017'
DB_NAME = 'url'


def db():
    from pymongo import MongoClient
    con = MongoClient(MONGO_URL, connectTimeoutMS=1000)
    return con[DB_NAME]
