2-3 pipenv安装及相关命令

2-4 开发工具推荐

2-5 开发工具配置
    pipenv --venv                                                                         2 ↵  2063  13:39:51 13/11/2018
    /Users/omega/.local/share/virtualenvs/fisher-OnIzNnPF
    在pycharm中设置project interpreter添加

2-6 flask最小原型及唯一URL原理（路由和重定向原理）



2-7 路由的另一种注册方法(自动重启)


2-8 app.run相关参数与flask配置文件
    导入配置文件:1、from config import DEBUG
                2、app.config.from_object('config')
    # __name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。当模块被直接运行时，代码将被运行，当模块是被导入时，代码不被运行。
    if __name__ == '__main__':
    # 在生产环境上一般不用flask自带的app部署。而是采用 nginx + uwsgi.


3-3 搜索关键字
    路由地址传递参数
    多条件判断中的条件出现的先后顺序对代码的执行效率有影响

3-4 简单的重构
    将业务判断逻辑封装到helper文件的函数中
    从而简化了视图函数，提高可读性
    过多的注释并咩有用

3-5 requests发送http请求及代码的简化手段
        简化代码的两种方式
        1、封装到函数中
        2、三元表达式封装if else

3-6 requests vs urllib
    requests更精简,更规范
    类写继承class HTTP():
    和不写继承的关系class HTTP:在Python3中没有区别

3-7 定义yushu_book获取url的返回数据

3-8
    通过flask自带的jsonify处理返回值，比json方法精简

3-9 将视图函数拆分到单独的文件中app/web/book.py
""" 如果这在里引入fisher的app实例，fisher会当做一个模块运行，最后的if判断中主函数名不是__main__
而是fisher。所以不会运行。如果再在Fisher里引用book.py则会导致循环引用后启动的app找不到book中的路由 """
