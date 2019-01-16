# -*- coding: utf-8 -*-
# @Time    : 2019-01-16 14:45
# @Author  : 张皓
# @Email   : zhanghao12z@163.com
# @File    : drift.py
# @Software: PyCharm


class DriftViewModel:
    def __init__(self, drift, current_user_id):
        self.data = {}

    # 判断是索要者还是赠送者
    @staticmethod
    def requester_or_gifter(self, drift, current_user_id):
        # 不这么写是因为，这样写会破坏类的封装性，对current_user有强依赖，导致强耦合
        # if drift.requester_id == current_user.id:
        if drift.requester_id == current_user_id:
            you_are = 'requester'
        else:
            you_are = 'gifter'
        return you_are

    def parse(self, drift, current_user_id):
        you_are = self.requester_or_gifter(drift, current_user_id)

        r = {
            'you_are': you_are,
            'drift_id': drift.id,
            'book_title': drift.book_title,
            'book_author': drift.book_author,
            'book_ img': drift.book_img,
            'date': drift.create_datetime.strftime('%Y-%m-%d'),
            'operater': drift.gifter_nickname if you_are == 'gifter' esle drift.requester_nickname,
            'message': drift.message,
            'address': drift.address,
            'recipient_name': drift.recipient_name,
            'mobile': drift.mobile,
            'status': drift.pending
        }