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
def send_async_email(msg):
    try:
        mail.send(msg)
    except:
        pass

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
    thread_send = Thread(Target=send_async_email, args=[msg])
    thread_send.start()
