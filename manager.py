# -*- coding:utf-8 -*- 
# Author: json_steve

from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)


# 配置类
class Config(object):
    """配置类信息"""
    #SECRET_KET = 'OZiDpgU1ir/pmSs8nFoqs6Z63RcupX58VhmiYQ0/DQDTiyXs1+duo6EY29SI1Xe4'
    SECRET_KEY = "bxOaxOKPaeZaipSvq7rjfeYtYvG5jPvwIgGZsteuTGhTSrKAHh/Q6eGHQm2Yw671"
    DEBUG = True
    # redis链接配置,配置信息在这里，被自己调用
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # mysql配置 看文档
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome18"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

app.config.from_object(Config)
# 初始化redis
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0)
# 数据库初始化 顺序很重要，在config之后
db = SQLAlchemy(app)
# csrf初始化
csrf = CSRFProtect(app)


@app.route('/', methods=["GET", 'POST'])
def index():
    redis_store.set(name='xiaoli', value='32')
    return 'index'


if __name__ == '__main__':
    app.run()


