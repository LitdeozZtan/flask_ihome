# -*- coding:utf-8 -*- 
# Author: json_steve

from flask import Flask,current_app,session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from config import Config

app = Flask(__name__)

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


