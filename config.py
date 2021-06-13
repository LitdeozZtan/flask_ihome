# -*- coding:utf-8 -*- 
# Author: json_steve
import redis


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