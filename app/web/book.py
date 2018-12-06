#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Nov 22, 2018 10:55
Author  : 张皓
Email   : zhanghao12z@163.com
Function:
===========================================
调用方法
Template:
===========================================
"""
import json

from flask import jsonify, request
from app.libs.helper import is_isbn_key
from app.spider.yushu_book import YuShuBook

# 导入验证层，判断参数是否合法
from app.forms.book import SearchForm
from . import web

# 导入ViewModel处理书籍数据
from app.view_models.book import BookViewModel, BookCollection


@web.route('/test')
def test():
    from .nolocal import n

    print('引入自定义的非线程隔离的变量原始值V：%s' % n.v)
    n.v = 2

    print('request线程隔离的变量原始值：%s' % getattr(request, 'v', None))
    setattr(request, 'v', 3)
    print('request线程隔离更新后的变量V：%s' % getattr(request, 'v', None))
    print('非线程隔离的变量更新后V：%s' % n.v)
    print('=======================')
    return ''

'''
# @web.route('/book/search/<q>/<page>')
@web.route('/book/search')
def search():
    """ q:用户传递的参数
        page:用户传递的页面
    """
    # 通过验证层判断参数是否合法
    form = SearchForm(request.args)
    if form.validate():
        # 取出验证后的值,并去除前后的值
        q = form.q.data.strip()
        page = form.page.data
        # 判断用户传入的参数是否为isbn
        isbn_or_key = is_isbn_key(q)
        if isbn_or_key == 'isbn':
            # 在pycharm中选择YuShuBook安住option+enter可以自动导入类
            result = YuShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)
        # 通过json模块处理返回结果
        # return json.dumps(result), 200, {'content-type': 'application/json'}
        # 通过flask自带的jsonify处理,效果同上
        return jsonify(result)
    else:
        # 返回自定义的错误返回
        # return jsonify({'msg': '参数校验失败'})
        return jsonify(form.errors)
'''

# 重构 从面向过程到面向对象进行重构2018-12-06 17:49:48
@web.route('/book/search')
def search():
    """ q:用户传递的参数
        page:用户传递的页面
    """
    # 通过验证层判断参数是否合法
    form = SearchForm(request.args)
    books = BookCollection()  # 实例化修整的数据类

    if form.validate():
        # 取出验证后的值,并去除前后的值
        q = form.q.data.strip()
        page = form.page.data
        # 判断用户传入的参数是否为isbn
        isbn_or_key = is_isbn_key(q)

        yushu_book = YuShuBook()  # 实例化鱼书book

        if isbn_or_key == 'isbn':
            # 在pycharm中选择YuShuBook安住option+enter可以自动导入类
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__, ensure_ascii=False)
        # return jsonify(books)
    else:
        # 返回自定义的错误返回
        # return jsonify({'msg': '参数校验失败'})
        return jsonify(form.errors)
