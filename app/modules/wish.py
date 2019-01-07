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
from sqlalchemy.orm import relationship


from app.spider.yushu_book import YuShuBook
from .base import Base, db
from sqlalchemy import String, Integer, ForeignKey, Boolean, Column, SmallInteger, desc, func


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book . relationship( ' Book' )
    # bid = Column(Integer, ForeignKey( 'user.id' ))
    # 手否赠送
    launched = Column(Boolean, default=False)

    # 查询用户的心愿清单
    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(
            uid=uid, launched=False).order_by(desc(
            Wish.create_time)).all()
        return wishes

    # 获取isbn对应的想要的用户数
    @classmethod
    def get_gitfs_count(cls, isbn_list):
        # 根据传入的一组isbn，到Wish表中检索出相应的礼物
        # 并算出某个礼物的赠送数量
        # filter_by传入关键字参数
        # filter传入条件表达式
        count_list = db.session.query(
            func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1).group_by(Gift.isbn).all()
        # count_list返回的是一个元组，格式化为字典
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    # 查询isbn对应的书籍
    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

# 避免循环导入
from app.modules.gift import Gift