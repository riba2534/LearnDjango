# Django学习笔记

本笔记为在`Django==2.0`环境下的学习笔记

操作系统为:`Deepin 15.7`

视频链接:[Django2.0教程](https://space.bilibili.com/252028233/#/)

进度 ： 06看完

## 创建项目

1. 创建项目:`django-admin startproject <项目名>`
2. 在本地执行服务器:`python3 manage.py runserver`
3. 在`urls.py`中规定访问的路径.
4. 创建超级管理员；`python3 manage.py createsuperuser`要注意密码不能太简单
5. 当有时候发生数据库的报错后，可以使用`python3 manage.py migrate`同步数据库
6. Django创建应用:`python3 manage.py startapp <应用名称>`
 


## 修改模型后改变数据库

1. 制造迁移:`python3 manage.py makemigrations`,实质上就是自动生成一个模型文件
2. 迁移:`python3 manage.py migrate`,自动生成一些sql语句

## 主键

1. `pk`是主键的意思,可以和主键混用


## 注意
1. `urls.py`可以写在具体的app里面
2. `__str__`方法可以改变后台管理界面的标题显示