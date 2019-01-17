#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Dec 4, 2018 16:35
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 书籍模型定义
===========================================
调用方法
Template:
===========================================
"""


# 重构后
class BookViewModel:
    """ 处理单个鱼书book的类 """
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = '' if book['pages'] is None else book['pages']
        self.author = '、'.join(book['author'])
        self.price = book['price']
        self.isbn = book['isbn']
        self.summary = book['summary'] or ''
        self.image = book['image']
        self.pubdate = book['pubdate']
        self.binding = book['binding']

    # 因为这个方法返回的是具体的数据，所以可以用装饰器来让这个方法让类像访问变量一样访问方法 BookViewModel.intro
    @property
    def intro(self):
        intros = filter(lambda x: x if True else False, [self.author, self.publisher, self.price])

        return '/'.join(intros)


class BookCollection:
    """ 处集合 鱼书book的类 """
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.book]



'''
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

'''