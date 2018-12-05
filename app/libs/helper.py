# -*- coding: utf-8 -*-
# @Time    : 2018/11/14 10:22
# @Author  : 张皓
# @Email   : zhanghao12z@163.com
# @File    : helper.py
# @Software: PyCharm


def is_isbn_key(word):
    """ 判断用户搜索的关键字是否为isbn """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key




