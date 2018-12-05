2-3 pipenv安装及相关命令

2-4 开发工具推荐
    虚拟python环境  
    进入pipenv shell

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

4-1 应用、蓝图与视图函数

app（核心对象）相当于插座 可以对应多个蓝图，也可以对应静态文件 视图函数 模板
蓝图也可以对应多个静态文件 视图函数 模板

核心对象的初始化可以放在__init__.py的文件

4-2 用蓝图注册视图函数
    from app.web.book import web
    app.register_blueprint(web)
4-3 单蓝图多模块拆分
    蓝图初始化放入到蓝图的__init__中，
    并在__init__中导入注册的模块，这样就可以实现单蓝图多个模块的导入

4-4 requests的导入方法
    更优雅的传入参数，requests需要在视图函数中
    # request需要在视图函数的上下环境中才能得到我们想要的预期结果
    ?q=&page=
    request.args['page'] 类型是immutablemultiDict 不可变字典
    不可变字典转可变字典 a = request.args.to_dict()

4-5 验证传递参数的合法性
    导入WTForms来验证参数的合法性
    如：q = StringField(validators=[Length(min=1, max=30, message='自定义q的错误提示')])
    验证参数q的最小和最大长度，并自定义错误提示
    返回return jsonify(form.errors)错误
    #添加多个验证器， DataRequired()可以识别空格  报：This field is required.
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])

4-6 配置文件的拆分

    将类里的参数，拆分到配置文件中
    拆分成两个配置文件：
    setting 存放普通的配置变量
    secure 存放比较机密的 如数据库连接信息

4-7 调整层级结构
    把httper和helper这些辅助类调整到app下的libs目录
    把yushu_book调整到app下spider下
    安装xampp启动本地mysql 用户名root 密码为空
    sudo /Applications/XAMPP/xamppfiles/bin/mysql.server start
    日志：/Applications/XAMPP/xamppfiles/var/mysql
    排查/Applications/XAMPP/xamppfiles/var/mysql/localhost.err日志，发现是相关目录和文件无写入权限
    sudo chmod -R 777 /Applications/XAMPP/xamppfiles/temp/mysql/
    sudo chmod -R 777 /Applications/XAMPP/xamppfiles/var/mysql

    create user mstx@localhost
      identified by 'mstx';
    直接创建用户并授权的命令
    grant all on *.* to mstx@localhost
    identified by  'mstx';
    新建一个数据库fisher
    数据表创建方式：
        1、database first （手动创建表和字段）
        2、model first （用建模工具创建表）
        3、code first (这次的重点)

4-8 引入模型层
    from sqlalchemy import Column, Integer, String
    通过调用sqlalchemy初始化花app.module.Book类的相关参数

4-9 将模型映射到数据库
    定义好基本变量后需要从flask_sqlalchemy去实例化sqlalchemy
    db = sqlalchemy()
    实例化后需要在Book类引用 Book(db.module)
    pipenv install cx_Oracle 
    pipenv install cymysql 
    pipenv install pymysql 
    在secure配置文件中配置数据库连接,本课程是使用cymysql
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://mstx:mstx@localhost:63306/fisher'
    含义是: 数据库类型 + 数据库驱动 + 用户名 + 密码 + 数据库IP + 端口号 + 数据库名
    pipenv install cymysql  


4-10 ORM和Code First
    Code First 可以让我们只专注于业务模型设计，表关系由我们的业务来觉得
    业务逻辑再Model层设计
    ORM 对象关系映射  通过操作模型来操作数据库

5-1 flask中经典错误 working outside application context

    应用级别的上下文 Flask
    请求级别的上下文 request
    两者都是对象

    通过设计模式的代理模式（localproxy）实现间接操作核心对象的功能



5-4 with语句是个语法糖
    一个对象有__enter__和__exit__方法时
    可以对一个实现了上下文协议的对象被称为“上下文管理器”可以使用with
    上下文表达式必须要返回一个上下文管理器
    with语句实现资源的管理

    with常见使用场景：
        文件的读写
        数据库的操作
    
    with后面的语法叫上下文表达式
    with .... as f :
        pass


6-1 什么是进程
    每个程序至少有一个进程，进程是竞争计算机资源的基本单位
    进程的上下文是很消耗资源的
    上下文是为了保存当前程序的状态

6-2 什么是线程
    进程是用来分配资源
    线程是用来利用资源
    多线程可以更高效的利用资源
    线程本身不拥有资源
    线程可以访问进程资源

6-3 多线程
    是为了充分利用cpu的性能优势 特别是多核
    引入threading


6-4 多线程的优势和好处

    多核的多线程执行相当于实现并行执行程序，提高了程序运行的速度

    Python不能充分利用多核cpu的性能

    Python的多线程是鸡肋？

6-5 全局解释器锁
    GIL GLOBAL INTERPRETER LOCK 一个cpu核同一时间只能执行一个线程
    因为多个线程会共享进程资源
    锁是为了保证线程安全

    锁分两种：
        细粒度锁  程序员级
        粗力度锁  解释器级 GIL

    Python有cpython和jpython。
    cpython默认有GIL,在一定程度上保证了线程安全
    但当代码被翻译成字节码bytecode时是会变成多段的字节码，如果多段之前间断，也会出现线程不安全

6-6 对应IO密集型程序，多线程是有意义的
    针对于cpu密集型的操作，Python的多线程是鸡肋，因为同一时间只能执行一个线程
    IO密集型程序
        计算圆周率
        视频解码

    但对于IO密集型程序
    如：查询数据库、请求网络资源、读写文件

6-7 flask的多线程机制和存在的问题

    web服务器
        nginx  apache tomcat IIS
    app.run()是内置的webserver 是单进程和单线程的模式
    一般部署到生产环境会用nginx
    开启多线程后存在的问题可能会造成数据污染
    因为一个request对象赋值给一个变量，但是多线程的话就会导致变量指向的不确定性
    一个变量名实例化为三个对象

6-8 线程隔离

    实现线程隔离的话
    Python中可以通过字典dictionary这种数据结构来标识多线程
    dict{'request1':'', "request2":""......}

6-9 线程隔离对象Local
    字典只是保存数据
    还需要操作数据

    from werkzeug.local import Local

    #引入线程隔离
    obj = Local()
    这样主进程和子进程就会不相互影响
    new_t = threading.Thread(target=worker,name='子进程')
    new_t.start()

    线程隔离的是变量的值
    storage{'ident':{'name':'value'}}

6-10 线程隔离的栈：LocalStack
    

6-11 LocalStack的基本用法
    from werkzeug.local import LocalStack
    引入实例化
    s = LocalStack()
    推入栈
    s.push(1)
    取出栈
    s.pop(1)
    调用栈顶
    s.top

6-12 LocalStack作为线程隔离对象的意义
    让指定对象找到对应的变量