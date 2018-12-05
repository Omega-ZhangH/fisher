#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Dec 4, 2018 16:35
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 预处理API的返回数据
===========================================
调用方法
Template:
===========================================
"""

class  BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }

        if data:
            returned['total'] = 1
            returned['books'] = cls.__cut_book_data(data)
            return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': '' if data['pages'] is None else data['pages'],
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image'],
        }

        return book

