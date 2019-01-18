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

from flask import jsonify, request, render_template, flash
from flask_login import current_user

from app.libs.helper import is_isbn_key
from app.modules.gift import Gift
from app.modules.wish import Wish
from app.spider.yushu_book import YuShuBook

# 导入验证层，判断参数是否合法
from app.forms.book import SearchForm
from app.view_models.trade import TradeInfo
from . import web

# 导入ViewModel处理书籍数据
from app.view_models.book import BookViewModel, BookCollection


# 2018-12-10 17:50:46
# 新增访问模板的视图函数
@web.route('/temp')
def test1():
    r = {
        'name': '张皓',
        'age': 27
    }
    class m:
        def __init__(self):
            self.name = '张皓'
    n = m()
    flash('正常消息闪现')
    flash('错误消息闪现', category='error')

# 模板 html
    return render_template('test4.html', data=r, n=n)


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
        # return json.dumps(books, default=lambda o: o.__dict__, ensure_ascii=False)
        # return jsonify(books)
    else:
        # 返回自定义的错误返回
        # return jsonify({'msg': '参数校验失败'})
        # return jsonify(form.errors)
        flash('搜索关键字不符合要求，请重新输入关键字')
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    # 判断是否在赠送和心愿清单
    has_in_gifts = False
    has_in_wishes = False

    # 取数据的详情页面
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    print(book.image)

    # 判断用户是否登录，是否在用的心愿和礼物清单
    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    # 查询数据库的模型数据
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    # 规整模型数据
    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html',
                           book=book,
                           wishes=trade_wishes_model,
                           gifts=trade_gifts_model,
                           has_in_wishes=has_in_wishes,
                           has_in_gifts=has_in_gifts)

