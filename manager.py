# -*- coding:utf-8 -*- 
# Author: json_steve

from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from iHome import app, db, redis_store


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


