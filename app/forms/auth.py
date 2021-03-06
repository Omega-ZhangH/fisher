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
from wtforms.validators import Length, DataRequired, Email, ValidationError, EqualTo

from app.modules.user import User


class EmailForm(Form):
    """
    校验输入的邮箱
    """
    email = StringField(validators=[DataRequired(), Length(8, 64),
                        Email(message='电子邮件不符合规范')])


class LoginForm(EmailForm):
    """
    继承EmailForm
    拥有Email用户邮箱校验
    """
    # email = StringField(validators=[DataRequired(), Length(8, 64),
    #                     Email(message='电子邮件不符合规范')])

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


class ResetPasswordForm(Form):
    """
    检测重置密码的两次密码是否一致
    """
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message='密码长度度至少需要在6到32个字符之向'),
        EqualTo('password2', message='两次输入的的密码不相同')])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)])
