# -*- coding: utf-8 -*-
# @Time    : 2019-01-15 14:59
# @Author  : 张皓
# @Email   : zhanghao12z@163.com
# @File    : enums.py.py
# @Software: PyCharm

from enum import Enum


class PendingStatus(Enum):
    """
        定义交易状态
    """
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4
