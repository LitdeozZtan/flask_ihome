# -*- coding:utf-8 -*- 
# Author: json_steve

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()