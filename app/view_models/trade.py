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


class TradeInfo:
    """
    处理赠送的礼物的数据规整
    """
    def __init__(self, goods):
        self.total = 0
        self.trade = []
        self._parse(goods)

    def _parse(self, goods):
        self.total = len(goods)
        self.trade = [self._map_to_trade(single) for single in goods]

    def _map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )
