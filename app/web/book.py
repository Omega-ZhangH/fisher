# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 15:37
# @Author  : 张皓
# @Email   : zhanghao12z@163.com
# @File    : book.py.py
# @Software: PyCharm
# 路由地址传递参数
from flask import jsonify, Blueprint
from helper import is_isbn_key
from yushu_book import YuShuBook

"""
from fisher import app
 如果这在里引入fisher的app核心对象，fisher会当做一个模块运行，最后的if判断中主函数名不是__main__
而是fisher。所以不会运行。如果再在Fisher里引用book.py则会导致循环引用后启动的app找不到book中的路由 
"""

# 实例化蓝图对象，并导入蓝图 变量为蓝图的名称和模块包
web = Blueprint('web', __name__)


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """ q:用户传递的参数
        page:用户传递的页面
    """
    # 判断用户传入的参数是否为isbn
    isbn_or_key = is_isbn_key(q)
    if isbn_or_key == 'isbn':
        # 在pycharm中选择YuShuBook安住option+enter可以自动导入类
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    # 通过json模块处理返回结果
    # return json.dumps(result), 200, {'content-type': 'application/json'}
    # 通过flask自带的jsonify处理,效果同上
    return jsonify(result)
