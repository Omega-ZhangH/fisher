1、安装虚拟环境工具
pip3 install pipenv  

2、创建项目虚拟环境
pipenv install
"""
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
"""

3、进入虚拟环境
pipenv shell
虚拟环境的左右：隔离扩展包，比如：新项目需要flask版本是0.3；但老版本需要0.11.

4、安装Python包
pipenv install flask

""" 
Package      Version
------------ -------
Click        7.0
Flask        1.0.2
itsdangerous 1.1.0
Jinja2       2.10
MarkupSafe   1.1.0
pip          18.1
setuptools   40.6.0
Werkzeug     0.14.1
wheel        0.32.2
"""

5、退出虚拟环境
exit

6、卸载安装包
pipenv uninstall flask

7、查看安装包依赖关系
pipenv graph