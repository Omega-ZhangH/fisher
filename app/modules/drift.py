#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Jan 14, 2019 16:42
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 鱼漂--交易模型定义
===========================================
调用方法
Template:
===========================================
"""
from sqlalchemy import Column, Integer, String, SmallInteger

from app.libs.enums import PendingStatus
from app.modules.base import Base


class Drift(Base):
    """
        具体的交易模型
    """
    id = Column(Integer, primary_key=True)

    # 邮寄信息
    recipient_name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)

    # 书籍信息
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    # 请求者信息
    requester_id = Column(Integer)
    requester_nickname = Column(String(20))

    # 赠送者信息
    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))

    # 赠送状态（详见libs.enums.py）
    _pending = Column('pending', SmallInteger, default=1)

    @property
    def pending(self):
        # 转化为枚举类型
        return PendingStatus(self._pending)

    @pending.setter
    def pending(self, status):
        """
        :param status:为枚举类型
                    转换为数字类型
        """
        self._pending = status.value
