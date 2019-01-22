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

SECRET_KEY = 'e10adc3949ba59abbe56e057f20f883e'


# 数据库连接
USERNAME = ''
PASSWORD = ''
HOSTNAME = 'localhost'
PORT = 3306
DATABASE = 'fisher'

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/" \
         "{db}?charset=utf8".format(username=USERNAME,
                                    password=PASSWORD,
                                    host=HOSTNAME,
                                    port=PORT,
                                    db=DATABASE)


SQLALCHEMY_TRACK_MODIFICATIONS = True
