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


## virtualenv的使用方法

1. 创建:`virtualenv <虚拟环境名称>`
2. 启动:`Scripts/active`
3. 退出:`deactive`
4. 激活虚拟环境:[使用虚拟环境 Virtualenv](https://www.zmrenwu.com/post/3/)
5. linux下通过`source active`的方法激活虚拟环境

## pip一键导出和安装
1. `pip freeze` 当前环境下安装的所有的库
2. `pip freeze > requirements.txt`重定向到一个文件
3. `pip install -r requirements.txt`安装这个文件中的所有库


## 常用模板标签

![](https://i.loli.net/2018/11/16/5bee46aece661.png)

![](https://i.loli.net/2018/11/16/5bee476e29e38.png)

1. `block`和`endblock`的使用
2. `extends`引用文件,使用模板页面

## 模板文件设置建议

1. app文件放在app中
2. project文件放在外面，类似于全局变量

## CSS美化页面

1. 使用`{% load staticfiles %}`来加载静态文件

## `manage.py`的`shell`的使用

1. 进入方法:`python3 manage.py shell`
    常用的一些方法:
    ```python
    from blog.models import Blog
    from django.contrib.auth.models import User
    Blog.objects.all()#查看当前博客的所有对象
    Blog.objects.count()#查看当前博客数量
    Blog.objects.all().count() #等同上面
    blog=Blog()#实例化
    blog_type=BlogType.objects.all()[0]#获取到第一个分类
    user=User.objects.all()[0] #获取到第一个用户
    for i in range(1,31):#利用for循环批量添加博客
        blog=Blog()
        blog.title='for %s' % i
        blog.content='这是第%s篇文章！' % i
        blog.blog_type=blog_type
        blog.author=user
        blog.save()
    ```
2. 分页器
   ```python
   from django.core.paginator import Paginator#引入分页器
   from blog.models import Blog#引入模型
   blogs=Blog.objects.all()#得到模型
   paginator=Paginator(blogs,10)#分页器进行分页
   paginator.num_pages#得到页的数量
   paginator.page_range#得到具体页码
   page1=paginator.page(1)#定义一个第一页,可以用dir(page1)查看里面的具体方法
   page1.object_list#得到当前页的具体对象
   ```

3. filter筛选
   ![](https://i.loli.net/2018/11/29/5bffd23f91208.png)
   先进入shell模式:`python3 manage.py shell`
   ```python
   from blog.models import Blog
   Blog.objects.filter(title__icontains='python') #关键字包含
   Blog.objects.filter(id__in=[1,3,4,23]) # 在...之内
   ```
4. annotate注释
   ```python
   from django.db.models import Count
   context['blog_types'] = BlogType.objects.annotate(
        blog_count=Count('blog'))  # 博客分类的对应博客数量,为什么小写?
   ```

## 使用富文本编辑器

1. 17开始，使用了富文本编辑器,首先`pip3 install django-ckeditor`,其实同时安装了两个库，分别是`django-ckeditor-5.6.1`和`django-js-asset-1.1.0`
2. 注册应用，在`settings.py`中
3. 修改`models.py`:
   ```python
   from ckeditor.fields import RichTextField
   content = RichTextField() 
   ```
   然后`python3 manage.py makemigrations`和`python3 manage.py migrate`

## 图片上传功能

1. 17课讲的(16:34)，首先安装`pillow`,`pip3 install pillow`
2. ![](https://i.loli.net/2018/12/01/5c023b82d067b.png)
   

## 用图表展示数据

网站地址:[highcharts](https://www.highcharts.com/),中文官网:[hcharts](https://www.hcharts.cn/)

教程:[1 分钟上手 Highcharts](https://www.hcharts.cn/docs/start-helloworld)


## 缓存创建

1. `python3 manage.py createcachetable`

## 评论模块

1. 创建评论app,`python3 manage.py startapp comment`

## Django-form的使用

1. 创建`forms.py`,字段->html input标签，每个字段都有一个适当默认的`widget`类
代码:
```python
from django import forms
class NameForm(forms.Form):
    your_name=forms.CharField(label='Your Name',max_length=100)
```
2. 使评论框支持`ckeditor`编辑器,富文本表单
   ```python
   from ckeditor.widgets import CKEditorWidget
   text = forms.CharField(widget=CKEditorWidget(config_name='comment_ckeditor'))
   ```
   然后在`settings.py`中设置相应配置.
   ```python
   CKEDITOR_CONFIGS = {
    'comment_ckeditor': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ["TextColor", "BGColor", 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ["Smiley", "SpecialChar", 'Blockquote'],
        ],
        'width': 'auto',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,
            }
        }
   ```
## ajax异步和jquery

ajax是一种不刷新页面的异步提交方式

jquery选择器:
```javascript
$("#comment_form") //id选择器
$(this)//当前方法的对象
```
python3格式化时间:
```python
import time
time.strftime('%Y-%m-%d %H:%M:%S')
```
