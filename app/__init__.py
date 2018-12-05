#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Nov 15, 2018 15:30
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 把app的初始化作。在这里app是核心对象。
===========================================
调用方法
Template:
===========================================
"""

from flask import Flask
from app.modules.book import db


def create_app():
    """ 初始化核心对象和配置文件 """
    # 初始化核心对象
    app = Flask(__name__)
    # 导入配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
