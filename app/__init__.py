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
from flask_login import LoginManager

# 实例化用户登录管理模块
login_manager = LoginManager()


def create_app():
    """ 初始化核心对象和配置文件 """
    # 初始化核心对象
    app = Flask(__name__)
    # 导入配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    # 把用户登录管理模块注册到flask中
    login_manager.init_app(app)
    # 指定用户认证不通过后跳转到登录界面
    login_manager.login_view = 'web.login'
    # 跳转的登录界面的信息改为中文
    login_manager.login_message = '请先登录或注册'

    db.init_app(app)
    db.create_all(app=app)

    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
