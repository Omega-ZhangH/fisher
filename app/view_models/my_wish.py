#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Dec 26, 2018 17:05
Author  : 张皓
Email   : zhanghao12z@163.com
Function:
===========================================
调用方法
Template:
===========================================
"""
from app.view_models.book import BookViewModel


class MyWishes():
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        self.__wish_count_list = wish_count_list
        self.__gifts_of_mine = gifts_of_mine

        self.gifts = self.__parse()

    def __parse(self):
        temp_gift = []
        for gitf in self.__gifts_of_mine:
            my_gitf = self.__matching(gitf)
            temp_gift.append(my_gitf)
        return temp_gift

    def __matching(self, gift):
        count = 0
        for wish in self.__wish_count_list:
            if gift.isbn == wish['isbn']:
                count = wish['count']
        result = {
            'wishes_count': count,
            'book': BookViewModel(gift.book),
            'id': gift.id
        }
        return result
