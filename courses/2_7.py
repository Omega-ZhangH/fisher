from flask import Flask

app = Flask(__name__)


# 调用装饰器设置路由
@app.route('/hello')
# 视图函数也就是控制器
def hello():
    # 基于类的视图(即插视图)
    return 'Hello,world'


# debug=True 开启调试模式
# 好处是会把异常详细的打印出来，而且会自动重启服务
app.run(debug=True)
