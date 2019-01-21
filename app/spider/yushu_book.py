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


# 重构后
class YuShuBook:
    """  """
    # 鱼书API基地址
    base_url = 'http://t.yushu.im/v2/book/'
    # 豆瓣的基地址
    # base_url = 'https://api.douban.com/v2/book/'
    # 定义通过isbn查找的url
    # isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    isbn_url = base_url + 'isbn/{}'
    # 定义通过关键字查找的url
    # keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    keyword_url = base_url + 'search?q={}&count={}&start={}'

    # 定义用isbn查询的方法 之所以用静态方法是在视图函数中可以不用实例化，直接调用
    def __init__(self):
        self.book = []
        self.total = 0

    def __fill_single(self, data):
        if data:
            self.book.append(data)
            self.total = 1

    def __fill_collection(self, data):
        if data:
            self.book = data['books']
            self.total = data['total']

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)

        # -----适应豆瓣API的代码
        # result['isbn'] = result.pop('isbn10')
        # result['image'] = result['images']['small']
        # -----适应豆瓣API的代码

        self.__fill_single(result)

    # 用类方法定义用关键字查询的方法

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword,
                                      current_app.config['PER_PAGE'],
                                      self.calculate_start(page))
        result = HTTP.get(url)

        # -----适应豆瓣API的代码
        # for i in range(result['count']):
        #     result['books'][i]['isbn'] = result['books'][i]['isbn10']
        #     result['books'][i]['image'] = result['books'][i]['images']['small']
        # -----适应豆瓣API的代码

        self.__fill_collection(result)

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']

    @property
    def first(self):
        return self.book[0] if self.total >= 1 else None


# url = 'https://api.douban.com/v2/book/isbn/9787111378457'
# result = HTTP.get(url)
# # # result['isbn'] = result.pop('isbn10')
# print(result)


'''
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
'''