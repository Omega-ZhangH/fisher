#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Nov 22, 2018 13:57
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 填写一些常用参数配置 和生产环境保持一致
===========================================
调用方法
Template:
===========================================
"""
# 设置默认每页显示数
PER_PAGE = 15

# 提交一本书以后新增的鱼豆
BEANS_UPLOAD_ONE_BOOK = 0.5

# 最近上传显示30本书
RECENT_BOOK_COUNT = 30

# Email配置
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'mstx_zhanghao@163.com'
MAIL_PASSWORD = 'mstx220'
# MAIL_SUBJECT_PREFIX = '[鱼书]'
# MAIL_SENDER = '鱼书 <mstx_zhanghao@163.com>'