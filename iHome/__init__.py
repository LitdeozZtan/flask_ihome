# -*- coding:utf-8 -*- 
# Author: json_steve
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config
from flask_sqlalchemy import SQLAlchemy
import redis
from flask import Flask

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