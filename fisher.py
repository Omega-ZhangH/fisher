#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Nov 14, 2018 14:42
Author  : 张皓
Email   : zhanghao12z@163.com
Function:
===========================================
调用方法
Template:
===========================================
"""
from app import create_app

# 应用级别的初始化
app = create_app()

if __name__ == '__main__':
#    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=80)
    app.run(debug=app.config['DEBUG'])
