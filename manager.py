# -*- coding:utf-8 -*- 
# Author: json_steve

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 数据库初始化
db = SQLAlchemy(app)


# 配置类
class Config(object):
    DEBUG = True
app.config.from_object(Config)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()


