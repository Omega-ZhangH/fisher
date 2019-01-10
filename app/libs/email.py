#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Jan 10, 2019 16:43
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 发送邮件
===========================================
调用方法
Template:
===========================================
"""

from app import mail
from flask_mail import Message


def send_mail():
    msg = Message('鱼书邮件', sender='mstx_zhanghao@163.com', body='Test',
                  recipients=['zhanghao@msok.com'])
    mail.send(msg)
