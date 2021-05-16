# -*- coding:utf-8 -*- 
# Author: json_steve

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)
# 数据库初始化
db = SQLAlchemy(app)


# 配置类
class Config(object):
    """配置类信息"""
    DEBUG = True
    # redis链接配置,配置信息在这里，被自己调用
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
app.config.from_object(Config)
# 初始化redis
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()


