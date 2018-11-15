#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date    : Nov 14, 2018 11:32
Author  : 张皓
Email   : zhanghao12z@163.com
Function: 封装获取url的方法
===========================================
调用方法
Template:
===========================================
"""

import requests

class HTTP:
    #目前没有用到类变量和实例方法。和普通函数并没有实质区别
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        #获取返回的json格式的数据
        """ 
        if r.status_code==200:
            if return_json:
                return r.json()
            else:
                return r.text
        else:
            if return_json:
                return {}
            else:
                return ''
        """
        #用三元表达式简化以上注释的代码
        # 如果状态码返回不是200且return_json则返回字典空{}否则返回字符串空''
        if r.status_code !=200:
            return {} if return_json else ''
        # 如果状态码返回是200且return_json则返回json数据否则返回字符串    
        return r.json() if return_json else r.text
        
        
        
        
        
        
        
        
        
        isbn=http://t.yushu.im/v2/book/isbn/9787501524044






