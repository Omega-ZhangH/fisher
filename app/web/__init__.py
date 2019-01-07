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
from flask import Blueprint
web = Blueprint('web', __name__)


# 导入蓝图下的模块

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish

