# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 11:10
# @Author  : 张皓
# @Email   : zhanghao12z@163.com
# @File    : book.py.py
# @Software: PyCharm
# 构建验证层
from wtforms import Form, IntegerField, StringField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    """
    q : 验证字符长度为1到30
    page : 验证数字在1到99, 并设置默认值为第1页
    """
    #q = StringField(validators=[Length(min=1, max=30, message='自定义q的错误提示')])
    # DataRequired() 添加多个验证器，报：This field is required.
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
