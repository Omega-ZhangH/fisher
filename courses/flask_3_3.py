from flask import Flask


app = Flask(__name__)
# 第二种导入配置文件
app.config.from_object('config')
#app.config['DEBUG']的默认值是False,所以想要覆盖这个值就需要配置文件的参数全部为大写
print(app.config['DEBUG'])

# 路由地址传递参数
@app.route('/book/search/<q>/<page>')
def search(q, page):
    """ 
    q:代表普通关键字
    isbn：书号查询
    page:分页
    """
    # isbn 由isbn13(新:由13个0-9得数字组成)和isbn10（老，由10个0-9和-组成）两种
    # 多条件判断中的条件出现的先后顺序对代码的执行效率有影响
    # 如果前面的条件判断的有假的条件，则后面的判断就不执行了。进而提高了代码的执行效率
    isbn_or_key = 'key'#定义isbn类型
    #判断是否是isbn13 长度为13 且全是数字
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    #缩短q    
    short_q = q.replace('-', '')
    #判断是否是为isbn10
    if '-' in q and len(short_q)==10 and short_q.isdigit():
        isbn_or_key = 'isbn'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
