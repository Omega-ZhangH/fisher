# -*- coding: utf-8 -*-
# @Time    : 2019-01-16 14:45
# @Author  : 张皓
# @Email   : zhanghao12z@163.com
# @File    : drift.py
# @Software: PyCharm
from app.libs.enums import PendingStatus


class DriftCollection:
    def __init__(self, drifts, current_user_id):
        self.data = []

        self.__parse(drifts, current_user_id)

    def __parse(self, drifts, current_user_id):
        for drift in drifts:
            temp = DriftViewModel(drift, current_user_id)
            self.data.append(temp.data)


class DriftViewModel:
    def __init__(self, drift, current_user_id):
        self.data = {}

        self.data = self.__parse(drift, current_user_id)

    # 判断是索要者还是赠送者
    @staticmethod
    def requester_or_gifter(drift, current_user_id):
        # 不这么写是因为，这样写会破坏类的封装性，对current_user有强依赖，导致强耦合
        # if drift.requester_id == current_user.id:
        if drift.requester_id == current_user_id:
            you_are = 'requester'
        else:
            you_are = 'gifter'
        return you_are

    def __parse(self, drift, current_user_id):
        # 判断用户类型
        you_are = self.requester_or_gifter(drift, current_user_id)
        # 获取用户的状态释义
        pending_status = PendingStatus.pending_str(drift.pending, you_are)
        r = {
            'you_are': you_are,
            'drift_id': drift.id,
            'book_title': drift.book_title,
            'book_author': drift.book_author,
            'book_ img': drift.book_img,
            'date': drift.create_datetime.strftime('%Y-%m-%d'),
            'operater': drift.gifter_nickname if you_are == 'gifter' else drift.requester_nickname,
            'message': drift.message,
            'address': drift.address,
            'status_str': pending_status,
            'recipient_name': drift.recipient_name,
            'mobile': drift.mobile,
            'status': drift.pending
        }
        return r