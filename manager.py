# -*- coding:utf-8 -*- 
# Author: json_steve

from flask import Flask,current_app,session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)


# 配置类
class Config(object):
    """配置类信息"""
    # SECRET_KET = 'OZiDpgU1ir/pmSs8nFoqs6Z63RcupX58VhmiYQ0/DQDTiyXs1+duo6EY29SI1Xe4'
    SECRET_KEY = "bxOaxOKPaeZaipSvq7rjfeYtYvG5jPvwIgGZsteuTGhTSrKAHh/Q6eGHQm2Yw671"
    DEBUG = True
    # redis链接配置,配置信息在这里，被自己调用
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # mysql配置 看文档
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome18"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # session 的配置在点进去里
    SESSION_TYPE = "redis"
    # 设置保存到的redis，默认如果没设置话，Flask-Session会帮我们创建一个redis
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 签名
    SESSION_USE_SIGNER = True
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400

app.config.from_object(Config)
# 初始化redis
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0)
# 数据库初始化 顺序很重要，在config之后
db = SQLAlchemy(app)
# csrf初始化
csrf = CSRFProtect(app)
# 初始化，无返回值 因为通过flask里的session操作
Session(app)
# Manager初始化
manager = Manager(app)
# 迁移初始化 无返回值 同Session因为通过终端命令操作
Migrate(app, db)
# 添加迁移命令 调用之前名字是db
manager.add_command('db', MigrateCommand)


@app.route('/', methods=["GET", 'POST'])
def index():
    session['xiaowu'] = 22
    age = session.get('xiaowu')
    print(age)  # 22
    redis_store.set(name='xiaoli', value='32')
    return 'index'


if __name__ == '__main__':
    manager.run()


