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
from threading import Thread

from flask import current_app, render_template

from app import mail
from flask_mail import Message


# 异步发送邮件
def send_async_email(app, msg):
    """
    :param app: 传入flask核心对象
    :param msg: 传入发送邮件的具体内容
    """
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            print('邮件发送失败!' + e)


def send_mail(to, subject, template, **kwargs):
    """
    :param to: 收件人
    :param subject: 邮件标题
    :param template: 邮件HTML模板
    :param kwargs: html渲染参数 用户名和token
    """
    # 硬编码的测试邮件
    # msg = Message('鱼书邮件', sender='mstx_zhanghao@163.com', body='Test',
    #               recipients=['zhanghao@msok.com'])
    msg = Message('[鱼书]' + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    # mail.send(msg)
    # 开启新的线程，异步发送邮件。
    # 注意这里要用核心对象而不是代理对象，否则会导致因线程隔离，找不到对应的核心对象
    app = current_app._get_current_object()
    thread_send = Thread(target=send_async_email, args=[app, msg])
    thread_send.start()
