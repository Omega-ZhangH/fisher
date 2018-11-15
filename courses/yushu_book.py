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
from  httper import HTTP

class YuShuBook:
    """  """
    # 定义通过isbn查找的url
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    # 定义通过关键字查找的url
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    # 定义用isbn查询的方法
    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result


    # 用类方法定义用关键字查询的方法
    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result