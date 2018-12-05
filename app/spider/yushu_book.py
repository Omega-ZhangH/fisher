#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Nov 14, 2018 14:26
Author  : 张皓
Email   : zhanghao12z@163.com
Function:
===========================================
调用方法
Template:
===========================================
"""
from app.libs.httper import HTTP

# 导入当前的Flask app的核心对象
from flask import current_app

class YuShuBook:
    """  """
    # 定义通过isbn查找的url
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    # 定义通过关键字查找的url
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    # 定义用isbn查询的方法 之所以用静态方法是在视图函数中可以不用实例化，直接调用
    @staticmethod
    def search_by_isbn(isbn):
        url = YuShuBook.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    # 用类方法定义用关键字查询的方法
    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']