#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Nov 15, 2018 15:30
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 把web的初始化作为包。在这里web是蓝图。
===========================================
调用方法
Template:
===========================================
"""


# 初始化蓝图

from flask import Blueprint, render_template, Response

web = Blueprint('web', __name__)


# 监控有返回404状态码的返回，自动转到自定义的404(状态码可自定义）
@web.app_errorhandler(404)
def not_found(e):
    # 基于AOP的思想 面向切片编程(Aspect Oriented Programming的缩写，意为：面向切面编程)
    # 这样就可以不用在每一个出现404代码的地方编写了，在这里集中处理，使得代码更加的精简
    # 可以返回自定义的结果
    # return Response(response='^_^!啊哦！404啦',status=200,mimetype='text/html')
    return '^_^!啊哦！404啦,木有这个页面'
    # return render_template('404.html'), 404


# 导入蓝图下的模块

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish

