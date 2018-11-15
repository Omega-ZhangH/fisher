#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Nov 14, 2018 14:42
Author  : 张皓
Email   : zhanghao12z@163.com
Function:
===========================================
调用方法
Template:
===========================================
"""
from flask import Flask
from helper import is_isbn_key
from yushu_book import YuShuBook

app = Flask(__name__)
# 第二种导入配置文件
app.config.from_object('config')
#app.config['DEBUG']的默认值是False,所以想要覆盖这个值就需要配置文件的参数全部为大写
print(app.config['DEBUG'])

# 路由地址传递参数
@app.route('/book/search/<q>/<page>')
def search(q, page):
    """ q:用户传递的参数
        page:用户传递的页面
    """
    # 判断用户传入的参数是否为isbn
    isbn_or_key = is_isbn_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)

    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
