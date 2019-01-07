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
    配置文件：/Applications/XAMPP/xamppfiles/etc/my.cnf
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
    使当前线程能够正确到引用到他自己所创建的对象，而不是引用到其他线程所创建的对象。
    对象是保存变量状态的地方

# 2018-12-03 16:28:22
6-13 flask中被线程隔离的对象
    连续发起两次请求，开启前需要打开多线程threading=True
    @web.route('/test')
def test():
    from .nolocal import n

    print('引入自定义的非线程隔离的变量原始值V：%s' % n.v)
    n.v = 2

    print('request线程隔离的变量原始值：%s' % getattr(request, 'v', None))
    setattr(request, 'v', 3)
    print('request线程隔离更新后的变量V：%s' % getattr(request, 'v', None))
    print('非线程隔离的变量更新后V：%s' % n.v)
    print('=======================')
    return ''

6-14 梳理串接flask的一些名词

    Flask只有一个核心对象

    线程隔离对象：Local和LocalStack
    被线程隔离的对象：通过Local和LocalStack创建的对象

    以线程ID作为key的字典Local
    LocalStack是封装了Local的栈

    AppContext 和 RequestContext 封装位LocalStack

    current_app 当前核心对象指向的是当前核心对象上下文的栈顶元素的一个属性
    current_app --> LocalStack.top == AppContext top.app=Flask

    request 指的是栈顶元素下面的request请求对象
    request -> LocalStack.top = RequestContext top.request = Request

# 2018-12-04 16:25:31
7-1 ViewModel的基本概念
    ViewModel把原始数据整理成页面所需要的数据
    作用：
        裁剪：减少一些字段
        修饰：加一些字段
        合并：

7-2 使用ViewModel处理书籍数据 上
    新建一个目录app.view_models

    class BookViewModel:
        @classmethod
        def package_single():
            pass
        def package_collection():
            pass
        def __cut_book_data():
            pass

# 2018-12-05 09:21:06
7-3 使用ViewModel处理书籍数据 下
    列表推导式
    [ i*3 for i in data]
    三元表达式来判空
    'pages': '' if data['pages'] is None else data['pages']
    更简洁的是
    'summary': data['summary'] or '',


7-4 伪面向对象：披着面向对象外衣的面向过程
    类：
        描述特征：类变量、实例变量
        行为：方法
    一个类里面只有方法，没有变量。本质是面向过程

    面向对象：类是基本单位
    面向过程：函数式基本单位

    如果一个类里面存在大量的类方法和静态方法的话，大致可以判断这个类
    封装的不太成功


7-5 重构鱼书核心对象：YuShuBook 上
    YuShuBook重构 加入特征和行为
    类中新增两个私有类方法来处理返回的数据
    __fill_single
    __fill_collection

# 2018-12-06 14:49:59
7-6 重构鱼书核心对象：YuShuBook 下
    7_6_1:重构app.view_models.book
    
    BookCollection
    BookViewModel

    7_6_2:重构app.web.book
    books = BookCollection() #  实例化修整的数据类
    yushu_book = YuShuBook() # 实例化鱼书book
    books.fill(yushu_book, q)

    存在问题：
        返回的对象无法序列化

7-7 json序列化看代码解释权反转

    对象的一个方法__dict__，可以返回对象所有的实例变量以字典的方式返回

    代码解释权的反转
    print(json.dumps(books, default=lambda o : o.__dict__, ensure_ascii=False))
    如：
    json.dumps
    sorted
    filter

# 2018-12-07 09:03:18
7-8 详解单页面与网站的区别
    js、css（静态文件）
    HTML(模板)  } 服务器渲染
    数据        }

    把数据填入到html模板中就叫做服务器渲染

    数据展示流程：
    浏览器-》ViewFunc(视图函数)-> render(html +Data) (data并不需要一定为json格式)
              返回JS、CSS、HTML、图片 （静态文件）<--

    单页面和普通网站有什么区别:
    多页面网址数据的渲染是在服务器进行
    单页面是在客户端渲染和操作

8-1 静态文件访问原理
    新建app.static文件，放静态文件（图片、js、html）
    无需用视图函数就可以访问静态文件(原因是flask默认为为static注册一个视图函数)
    实例化核心对象的目录就是根目录,

    static文件夹默认在根目录下 
    可以自定义
    app = Fask(__name__, static_folder='view_models/statics',static_url_path='')

    应用程序的静态文件
    蓝图的静态文件
    在蓝图的初始化添加static

    静态文件夹建议在默认位置，以便于多蓝图共享

# 2018-12-10 17:38:00
8-2 模板文件位置与修改方案
    新建app.templates和下面加test.html
    flask 提供模板填充方法 
    render_template()
    参数：模板名,数据

    想更改模板文件夹的默认位置和名字的话，可以在核心对象实例化和蓝图实例化时
    通过默认参数来修改,比如放到app.web下
        app = Flask(__name__, template_folder='web/templates')
        web = Blueprint('web', template_folder='templates')
        注意 在核心对象和蓝图的时候写的路径是不一样的，这里写的是相对路径

    建议:如果有多蓝图可以设计多个模板文件夹

# 2018-12-11 09:29:39
8-3 Jinja2的概念
    用双花括号
    {{ data.age }}

8-4 Jinja2读取字典和对象
    用双花括号绑定数据
    {{ data.age }}

    data是一个字典，在模板语言离可以用.来访问，也可以用[]来访问
    同理，访问对象也可以用上面两种方式

8-5 Jinja2流程控制语句
    模板语言需要
    {% if %}
    {% endif %}
    如：
    {% if data.age < 18 %}
        {{data.age}}
    {% elif data.name == '张皓' %}
        do something
    {% else %}
        {{data.name}}
    {% endif %}
    -----------
    {% for in%}

8-6 Jinja2循环语句
    遍历字典
    {% for  k,v in data.items() %}
      {{ k,v }} # 出来的是元组
      <div>111</div>
    {% endfor %}

8-7 使用模板继承
    test3.html
    新建app.templates.layout.html
    <!--引入基础模板-->
    {% extends 'layout.html' %}
    # 指定区域
    {% block content %}
    <!--继承本有的值，并加入for循环的新值-->
    {{ super() }}
    {% endblock %}
    不加的话，则会替换本有的阈值

8-8 default过滤器与管道命令
    <!--过滤器，如果字典中没有这个key则返回未名-->
        {{ data.school | default('未名') }}
    
    # 如果data.name='',则返回的结果为True
    {% if data.age > 18 %}
        {{ data.name == None | default('未名') }}
    {% endif %}

    常用的过滤器还有first()、length()
    {{ data.name | length() }}
    也可以自己写过滤器

# 2018-12-12 19:12:50
8-9 反向构建URL
    url_for('',)
    引入css、图片等静态文件
    还可以指向视图函数的地址web.search
     <!--引入css文件的三种方法-->
    <!--<link rel="stylesheet" href="http://localhost:5000/static/test.css">-->
    <!--<link rel="stylesheet" href="/static/test.css">-->
    <link rel="stylesheet" href="{{ url_for('static', filename='test.css') }}">

# 2018-12-13 15:02:51
8-10 消息闪现、SecretyKey与变量作用域
    首先倒入flask的flash模块
    在配置文件中配置SECURE_KEY的值。
    定义消息闪现的内容
    flash('正常消息闪现')
    flash('错误消息闪现', category='error')

    两种消息闪现的模式
    <!--with的消息闪现-->
{% with error = get_flashed_messages(category_filter=['error']) %}
    {% if data.age > 18 %}
<!--过滤器，如果字典中没有这个key则返回未名-->
    {{ 'data.name的长度:' }}
    {{ data.name | length() }}
<div>错误消息闪现:</div>
    {{ error }}
    {% endif %}
{% endwith %}

    <!--消息闪现-->
            <div>正常的消息闪现:</div>
            {% set message = get_flashed_messages() %}
            {{ message }}

8-11 显示搜索结果页面
    把前端代码复制到静态文件夹和模板文件夹，
    在蓝图中添加各种函数视图


8-12 页面结构解析
    基础模板加载css一般放在顶部
    加载脚本的话一般放在页面的底部

# 2018-12-15 15:43:08
9-1 viewmodel意义的体现与filter函数的巧妙应用
    {{ book.summary | defaut('',True)}}:如果book.summary的取值是空值的话，就显示空值

    通过fliter过滤器
    s = filter(lambda x: x if True else False,[1,'',2])

    在bookViewModel添加一个书籍介绍的属性函数
    在类里加上装饰器property，就可以像访问类变量一样访问类方法的结果，是因为这方法返回的结果是一个数据，所以用这种方法
        @property
        def intro(self):
        intros = filter(lambda x: x if True else False, [self.author, self.publisher, self.price])

        return '/'.join(intros)

9-2 书籍详情页面业务逻辑分析
    书籍详情页面
	默认显示所有赠书人的名字
	点击“赠送此书” 
		确定用户身份为“赠书人”
			页面底部数据切换位索要人的名字
			把书籍加入到赠送清单
	点击“加入到心愿清单”
		确定用户身份为“索要者”
			把书籍加入到心愿清单

# 2018-12-17 17:09:50
9-3 实现书籍详情页面
    编写book_detail视图函数
    BookViewModel新增isbn属性
    优化：Yushubook编写一个first()属性方法返回book列表的第一个元素

# 2018-12-18 10:17:36
9-4 模型与模型关系
 
    用户模型 user.py
    书籍模型 book.py
    赠送模型 gify.py
    基础模型 base.py


from sqlalchemy import Column, Integer, String, Boolean, Float .

class User(db.Model):
    id = Column(Integer, primary_ key=True)
    niakname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column( Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column( Integer, default=0)
    receive_counter = Column( Integer, default=0)
    WX_ open_id = Column(String(50))
    WX_ name = Column(String(32))


from app.models.base import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy .orm import relat ionship

class Gift(db.Model):
    id = Column( Integer, primary_ key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user .id'))
    isbn = Column(String(15), nullable=False)
    # book . relationship( ' Book' )
    # bid = Column(Integer, ForeignKey( 'user.id' ))
    launched = Column(Boolean, default=False)



9-5 自定义基类模型
    定义一个基类模型，然后让不同的模型继承同样需要的字段，然后让不通的模型继承这个基类
db = SQLAlchemy()
class Base(db.Model):
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1) #用来标记用户赠送礼物状态的软删除，方便以后分析用户的行为

    class Gift(Base):
        pass
    
    class User(Base):
        pass

9-6 用户注册
    完善用户注册的思维导图
        用户系统
            登录
            注册
                邮件作为账号
            修改密码
            找回密码
    让视图函数支持GET和POST方法
    @web.route('/register', methods=['GET', 'POST'])
    让基类不创建表需要添加一个属性
    __abstract__ = True # 不创建表，只作为基类 不然会包没有主键


# 2018-12-19 20:36:30
9-7 Python的动态赋值
    通过在基类中配置一个set_attrs方法,实现用户提交的数据字典中
    key与数据库的字段相同话，直接动态赋值到模型中
        def set_attrs(self,attrs_dict):
        for k, v in attrs_dict.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)

9-8 Python属性描述符实现getter与setter
    SQLALCHEMY指定表名和字段名
    __tablename__ = 'user'
    _password = Column('password')
        要解决用户注册的明文密码，在数据库是加密存放的。
    通过getter(@property) 和setter(@password.setter)通过方法的形式对数据进行预处理 
    通过这个也可以实现只读的和只写的操作

9-9 ORM的方式保存模型
            # 把用户模型添加到数据库
        db.session.add(user)
        db.session.commit()

9-10 自定义验证器
    在form下面编写自定义的验证器
    WTForm会自动识别为你是要验证email
    方法名命名为validator_email()
    同样需要验证昵称 validator_nickname()
    查询是否数据库中存在数据用
    User.query.filter_by(email=field.data).first():
        raise ValidationError('电子邮箱已经被注册')

# 2018-12-21 11:39:06
9-11 redirect重定向
     用户注册成功后，重定向到新的登录页面
     redirect(url_for('web.login'))

9-12 什么是cookie？
    用户访问一个网站，验证完身份后就会把身份票据写入cookie，一段时间内可以免登陆。
    用户的登录流程
    登录
        验证身份
        颁布票据
            将票据返回给客户端
                将票据写入到cookie中
                    KEY:VALUE键值对
                    cookie有效期
        在一定时间内，每次访问网站，都携带票据

9-13 cookie的应用
    cookie的跨站共享，可以针对用户进行定制化广告推送
    在User模型中设定密码校验的函数。通过引入以下来实现
    from werkzeug import check_passord_hash

9-14 login_user 将用户信息写入cookie
    在app.__init__.py中的核心对象实例化中
    通过引入from flask_login import login_manager
    来管理用户的票据、cookie、权限

    # 实例化用户登录管理模块
    Login_manager = Login_manager()

    def create_app():
        ...
        #把用户登录管理模块注册到flask中
        Login_manager.init(app)
    通过在蓝图auth中引入from flask_login import  login_user
    login_user:很精妙 主要完成的就是用户的票据的颁发、cookie的写入、有效期的控制、权限的管理 

    #在User中定义用户唯一标识函数，使得Flask_login的login_user拿到唯一标识写入cookie
    def get_id(self):
        """
        函数名固定，需要个login_user中的保持一致
        如果自定义的模型中定义的用户唯一标识不是id,可以通过此覆盖login_user中的get_id()。
        :return: 用户的唯一标识
        """
        return self.id
# 2018-12-24 16:39:26
9-15 访问权限控制
    控制某些用户需要登录才能访问
    在需要控制的视图函数添加装饰器
    from flask_login import login_required
    在模型中让用户管理插件获取用户模型
    from app import Login_manager
    @login_manager.user_loader
    def get_user(uid):
        return User.query.get(int(uid))


9-16 重定向攻击
    在app.__init__
    # 指定用户认证不通过后跳转到登录界面
    login_manager.login_view = 'web.login'
    # 跳转的登录界面的信息改为中文
    login_manager.login_message = '请先登录或注册'
    
    if not next and not next.startswith('/'):
    防止重定向攻击：http://127.0.0.1:5000/login?next=http://www.qq.com

# 2018-12-25 15:48:18
10-1 鱼豆
    在app.models新增gift模型
    鱼豆
        经济系统
            虚拟货币
            积分
        每上传一本书	
            系统送0.5个
        索要一本书
            消耗一个
        成功赠送一本书
            获得一个

10-2 思维逻辑锻炼
    需要校验用户是否可以把该书放到心愿清单
        1、是否符合isbn规范
        2、是否存在该图书
        3、该用户既赠送者又是索要者
        4、不允许一个用户同时赠送多本图书
    
    做WEB不太需要数学基础和算法功底，但是需要较强的罗辑思维能力
    在User模型下写验证：
    def can_save_to_list(self, isbn):
        """
        判断是否符合保存到心愿清单的条件
        :param isbn:
        :return:
        """
        # 判断是否符合ISBN规范
        if is_isbn_key(isbn) != 'isbn':
            return False

        # 判断是否有这本书
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.total:
            return False

        # 判断是否在心愿清单或者赠送清单
        gifting = Gift.query.filter_by(id=self.id, isbn=self.isbn, launched=self.lunched).first()
        wishing = Gift.query.filter_by(id=self.id, isbn=self.isbn, launched=self.lunched).first()
        if not gifting and not  wishing:
            return False
        else:
            return True

10-3 事务与回滚
        事务回滚是为了保证数据的一致性。防止后续操作无法进行
        try:
            gift = Gift()
            gift.isbn = isbn
            gift.id = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
10-4 Python @contextmanager
    实现在函数中返回一个函数，等返回的外部函数执行完再回到函数中
    class My():
    # def __enter__(self):
    #     print('enter')
    #     return self
    # def __exit__(self, exc_type, exc_value, tb)
    #     print('EXIT')
    
    def query(self):
        print('query')

    from contextlib import contextmanager

    @contextmanager
    def make():

        print('enter')
        yield My()
        print('EXIT')

    with make() as M :
        M.query()

10-5 灵活使用@contextmanager
    实现巧妙的组合,包装成上下文管理器
    @contextmanager
    def s():
        print('《', end='')
        yield
        print('》')

    with s():
        print("中庸", end='')

10-6 结合继承、yield、contextmanager、rollback来解决问题
    
    重新包装SQLAlchemy，实现精简代码的效果。

    from contextlib import contextmanager


    class SQLAlchemy(_SQLAlchemy):
        @contextmanager
        def auto_commit(self):
            try:
                yield
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

10-7 类变量的陷阱
    类变量和实例变量
    类变量是在程序启动的时候就已经有值了
    实例变量是当你每次实例化一个类的时候产生的新的值
    class Base(db.Model):
        __abstract__ = True # 不创建表，只作为基类
        create_time = Column('create_time', Integer)
        status = Column(SmallInteger, default=1)

        def __init__(self):
            self.create_time = int(datetime.now().timestamp())

# 2018-12-26 11:10:52
10-8 合理使用ajax
    通过redirect重定向到本页。
    可以通过AJAX技术回到本页。节省服务器资源。

10-9 书籍交易视图模型
    处理书籍赠送的数据规整
    class TradeInfo:
    """
    处理赠送的礼物的数据规整
    """
    def __init__(self, goods):
        self.total = 0
        self.trade = []
        self._parse(goods)

    def _parse(self, goods):
        self.total = len(goods)
        self.trade = [self._map_to_trade(single) for single in goods]

    def _map_to_trade(self, single):
        return dict(
            user_name=single.user.nick_name,
            time=single.create_time.strftime('%Y-%m-%d'),
            id=single.id
        )


# 2018-12-27 14:38:40
10-10 处理时间
    由于single.create_time.strftime('%Y-%m-%d')中的需要是datetime类型
    所以在base中做属性转换
        # 将时间戳转为Python的datetime类型
    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

10-11 书籍详情页面
    def book_detail(isbn):
    # 判断是否在赠送和心愿清单
    has_in_gifts = False
    has_in_wishes = False

    # 取数据的详情页面
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    # 判断用户是否登录，是否在用的心愿和礼物清单
    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    # 查询数据库的模型数据
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    # 规整模型数据
    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html',
                           book=book,
                           wishes=trade_wishes_model,
                           gifts=trade_gifts_model,
                           has_in_wishes=has_in_wishes,
                           has_in_gifts=has_in_gifts)

10-12 再谈MVC中的Model
    模型层应该是写业务逻辑方法
    Models模型层可以再写三层
        Service
        Logic
        Model

10-13 重写filter_by

    重写基类的方式，来实现自己的业务逻辑
    在不修改源代码的情况下，修改自定义的基类覆盖原来的基类
    # 重写基类来实现自身的业务逻辑 自定义filter_by，添加默认属性
class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

db = SQLAlchemy(query_class=Query)

# 2018-12-29 15:31:41
11-1 最近的礼物（复杂SQL的编写方案）
    →四种方式
    第一种：写在Gift模型中，写入业务逻辑
    # 编写查询最近上传的礼物
    def recent(self):
        recent_gitf = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            Gift.create_time).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gitf
    第二种：写到视图函数中
    第三种：在模型中重新定义一个RecentGift

11-2 链式调用
    # 编写查询最近上传的礼物
    def recent(self):
        # 链式调用
        # 主体：Query
        # 子函数：group_by、order_by、limit
        # 触发语句：all()、first()
        # 优点：提供了极大的灵活性
        recent_gitf = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            Gift.create_time).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gitf

11-3 完成最近的礼物（业务的四种编写方案）
    良好的封装是优秀代码的基础
    app.web.main.py
    @web.route('/')
    def index():
        recent_gifts = Gift.recent()
        # 利用列表推导式完成isbn到书籍的转换
        books = [BookViewModel(gift.book) for gift in recent_gifts]
        return render_template('index.html', recent=books)

11-4 我的礼物 一 （使用db.session和filter做查询）
    Gitf模型处：
        # 查询用户的礼物清单
    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(
            uid=uid, launched=False).order_by(desc(
            Gift.create_time)).all()
        return gifts


11-5 我的礼物 二（group_by与funct.count统计联合使用）
        # 获取isbn对应的想要的用户数
    @classmethod
    def get_wish_count(cls, isbn_list):
        # 根据传入的一组isbn，到Wish表中检索出相应的礼物
        # 并算出某个礼物的心愿数量
        # filter_by传入关键字参数
        # filter传入条件表达式
        count_list = db.session.query(
            func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False, 
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(Wish.isbn).all()
        return count_list

# 2019-01-04 15:52:20
11-6 我的礼物 三 (不要在函数中返回元组，而应该返回字典)
    直接返回count_list是元组
            # count_list返回的是一个元组，格式化为字典
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

11-7 我的礼物 四
    编写app.view_models.my_gifts
    不建议在实例方法里修改实例变量。
    可以在实例方法里读取实例变量

    # 可以省去定义类和属性
    from collections import namedtuple

    my = namedtuple('my',['id','name'])
    mine = my('1','zhanghao')
    print(mine.id,mine.name)

11-8 用户注销
@web.route('/logout')
def logout():
    #通过 from flask_login import login_user, logout_user
    logout_user() #把浏览器的cookie清空
    return redirect(url_for('web.index'))
