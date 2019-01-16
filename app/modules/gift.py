#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Dec 4, 2018 16:35
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 赠送的礼物模型定义
===========================================
调用方法
Template:
===========================================
"""
from flask import current_app
from sqlalchemy.orm import relationship

from app.modules.base import db

from app.spider.yushu_book import YuShuBook
from .base import Base
from sqlalchemy import String, Integer, ForeignKey, Boolean, Column, desc, func


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book . relationship( ' Book' )
    # bid = Column(Integer, ForeignKey( 'user.id' ))
    # 手否赠送
    launched = Column(Boolean, default=False)

    # 判读是不是自己送出的礼物
    def is_yourself_gift(self, uid):
        return True if uid == self.uid else False


    # Gitf对象代表的是一个礼物
    # 编写查询最近上传的礼物
    # 类代表的是自然界中具体事物的抽象，不代表某一个
    @classmethod
    def recent(cls):
        # 链式调用
        # 主体：Query
        # 子函数：group_by、order_by、limit
        # 触发语句：all()、first()
        # 优点：提供了极大的灵活性
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift

    # 查询isbn对应的书籍
    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 查询用户的礼物清单
    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(
            uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    # 获取isbn对应的想要的用户数
    @classmethod
    def get_wish_count(cls, isbn_list):
        # 根据传入的一组isbn，到Wish表中检索出相应的礼物
        # 并算出某个礼物的心愿数量
        # filter_by传入关键字参数
        # filter传入条件表达式
        count_list = db.session.query(
            func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(Wish.isbn).all()
        # count_list返回的是一个元组，格式化为字典
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

# 避免循环导入
from app.modules.wish import Wish