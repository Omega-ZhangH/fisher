from flask import Flask

app = Flask(__name__)

# 调用装饰器设置路由
@app.route('/hello/')
# 视图函数也就是控制器
def hello():
    # 基于类的视图(即插视图)
    return 'Hello,world'
""" 
路由设置为@app.route('/hello')
    用户输入即可访问
    http://127.0.0.1:5000/hello
如果用户输入http://127.0.0.1:5000/hello/
    则需要将路由设置为@app.route('/hello/')
    原理:浏览器访问url正常情况下：
    浏览器 ----->url ------------->服务器
    浏览器 <-----返回数据和状态码200（status code:200） <-------------服务器
    而flask则用的是重定向原理:
    浏览器 ----->url ------------->服务器
    浏览器 <-----浏览器头header会有一个Location（重定向的地址）和状态码301或302（status code:301） <-------------服务器
    浏览器 ----->重定向后的url ------------->服务器
    浏览器 <-----返回数据和状态码200（status code:200） <-------------服务器
"""
app.run()