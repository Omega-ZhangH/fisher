#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Dec 18, 2018 11:42
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 用户模型定义
===========================================
调用方法
Template:
===========================================
"""
# 获取用户的标识相关信息
from flask_login import UserMixin
from app import login_manager

from sqlalchemy import Column, Integer, Boolean, Float, String

from app.modules.gift import Gift
from app.modules.wish import Wish
from app.spider.yushu_book import YuShuBook
from courses.helper import is_isbn_key
from .base import Base

from werkzeug import generate_password_hash, check_password_hash


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    _password = Column('password', String(128), nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        """
        :param raw: raw为用户传进来的明文密码
        :return: 返回的结果为设置模型的属性password为加密后的值
        """
        self._password = generate_password_hash(raw)

    # 检查用户密码
    def check_password(self, raw):
        """
        通过插件提供的方法比对用户输入的密码和数据库中加密的密码是否一致
        并返回True or False
        """
        return check_password_hash(self._password, raw)

    # 定义用户唯一标识函数，使得Flask_login的login_user拿到唯一标识写入cookie
    def get_id(self):
        """
        函数名固定，需要个login_user中的保持一致
        如果自定义的模型中定义的用户唯一标识不是id,可以通过此覆盖UserMixin中同名的父类方法get_id()。
        :return: 用户的唯一标识
        """
        return self.id

    def can_save_to_list(self, isbn):
        """
        判断是否符合保存到心愿清单的条件
        :param isbn:
        :return:
        """
        # 判断是否符合ISBN规范
        if is_isbn_key(isbn) != 'isbn':
            return False

        # 判断是否有这本书
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False

        # 判断是否在心愿清单或者赠送清单
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        # print('''=======
        # %s
        # =======''' % gifting.__dict__)
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
