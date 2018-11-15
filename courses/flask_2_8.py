from flask import Flask


app = Flask(__name__)
# 第一种引入配置文件
#from config import DEBUG

# 第二种导入配置文件
app.config.from_object('config')
#app.config['DEBUG']的默认值是False,所以想要覆盖这个值就需要配置文件的参数全部为大写
print(app.config['DEBUG'])

# 调用装饰器设置路由
@app.route('/hello')
# 视图函数也就是控制器
def hello():
    # 基于类的视图(即插视图)
    return 'Hello,world'


# 为什么加if？
# 在生产环境上一般不用flask自带的app部署。而是采用 nginx + uwsgi.
# 如果不加if判断是不是入口文件.就会在生产环境中启动flask自带的服务器。造成启动了两个服务器
# print(__name__)在被引用导入的时候会显示为模块名。
# 如果是被直接执行则显示的为 __main__
# __name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。当模块被直接运行时，代码将被运行，当模块是被导入时，代码不被运行。
if __name__ == '__main__':
# 生产环境的代码和开发环境的代码一定是一模一样的镜像文件,避免用户展示出debug的方法是编写配置文件
# from导入配置文件
# app.run(host='0.0.0.0', debug=DEBUG, port=81)
###################
# app.config导入配置文件

    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
