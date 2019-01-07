#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Dec 18, 2018 20:49
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 构建用户注册的验证层
===========================================
调用方法
Template:
===========================================
"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, Email, ValidationError

from app.modules.user import User


class LoginForm(Form):
    """
    用户登录校验的类
    """
    email = StringField(validators=[DataRequired(), Length(8, 64),
                        Email(message='电子邮件不符合规范')])

    password = PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])


class RegisterForm(LoginForm):
    """
    用户注册校验的类
    """
    #
    # email = StringField(validators=[DataRequired(), Length(8, 64),
    #                     Email(message='电子邮件不符合规范')])
    #
    # password = PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])

    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称至少两个字符，最多10个字符')])

    def validate_email(self, field):
        """
        :param field: WTForms会自动传入field
        :return:
        """
        # 查询用户的邮箱是否已注册
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已注册')

    def validate_nickname(self, field):
        """
        :param field: WTForms会自动传入field
        :return:
        """
        # 查询用户的邮箱是否已注册
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('用户昵称已注册')
