#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Dec 18, 2018 10:53
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 基础模型定义
===========================================
调用方法
Template:
===========================================
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, SmallInteger, Integer

from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):
    """
    用with语法实现提交数据库自动提交和回滚，精简代码量
    """
    @contextmanager
    def auto_commit(self):
        try:
            yield
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


# 重写基类来实现自身的业务逻辑 自定义filter_by，添加默认属性
class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)
# db = SQLAlchemy(query_class=Query,  use_native_unicode="utf8")


# 定义基类
class Base(db.Model):
    __abstract__ = True  # 不创建表，只作为基类
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    # 放在基类中，继承基类的类就有这个方法了。 方便保存和模型一致的名字的数据保存到数据库
    def set_attrs(self, attrs_dict):
        for k, v in attrs_dict.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)

    # 将时间戳转为Python的datetime类型
    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    # 编写状态设置为回滚
    @staticmethod
    def delete(self):
        self.status = 0