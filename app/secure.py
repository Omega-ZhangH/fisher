#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Nov 22, 2018 13:57
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 填写数据库密码
          设置比较机密的信息
          以及和生产环境不一致的配置信息
          这个不要上传到git仓库
===========================================
调用方法
Template:
===========================================
"""
# 常量通常是大写。配置文件的参数都大写
DEBUG = True
# 本地数据库连接
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://mstx:mstx@localhost:63306/fisher'

# 民生数据库连接
#SQLALCHEMY_DATABASE_URI = 'oracle://SYSTEM:"Mstx@2018."@172.16.53.11:1521/ORCL'

SQLALCHEMY_TRACK_MODIFICATIONS = True
# DEBUG = False

SECRET_KEY='e10adc3949ba59abbe56e057f20f883e'