# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 11:10
# @Author  : 张皓
# @Email   : zhanghao12z@163.com
# @File    : book.py.py
# @Software: PyCharm
# 构建验证层
from wtforms import Form, IntegerField, StringField
from wtforms.validators import Length, NumberRange, DataRequired, Regexp


class SearchForm(Form):
    """
    q : 验证字符长度为1到30
    page : 验证数字在1到99, 并设置默认值为第1页
    """
    #q = StringField(validators=[Length(min=1, max=30, message='自定义q的错误提示')])
    # DataRequired() 添加多个验证器，报：This field is required.
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


class DriftForm(Form):
    """
        定义鱼漂页面的数据检测
    """
    recipient_name = StringField(validators=[DataRequired(), Length(
        min=2,
        max=20,
        message='收件人姓名长度必须在2到20个字符之间')])

    mobile = StringField(validators=[DataRequired(), Regexp('^1[0-9]{10}$', 0, '请输入正确的手机号码')])

    message = StringField()

    address = StringField(validators=[DataRequired(), Length(
        min=10,
        max=70,
        message='地址还不到10个么？尽量写详细一些吧')])
