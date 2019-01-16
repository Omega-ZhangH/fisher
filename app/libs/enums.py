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

    @classmethod
    def pending_str(cls, status, key):
        """
        :param status: pending的状态
        :param key: 输入是索要者还是赠送者
        :return: 返回最终的文本结果
        """
        key_map = {
            1: {
                'requester': '等待对方邮寄',
                'gifter': '等待你邮寄'
            },
            3: {
                'requester': '对方已拒绝',
                'gifter': '你已拒绝'
            },
            4: {
                'requester': '你已撤销',
                'gifter': '对方已撤销'
            },
            2: {
                'requester': '对方已邮寄',
                'gifter': '你已邮寄，交易完成'
            }
        }

        return key_map[status][key]