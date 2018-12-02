from django.db import models
from django.contrib.auth.models import User
from read_statistics.models import ReadNumExpandMethod

from mdeditor.fields import MDTextField


class BlogType(models.Model):  # 博客分类
    type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.type_name


class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)  # 标题
    content = MDTextField()  # 内容
    blog_type = models.ForeignKey(
        BlogType, on_delete=models.DO_NOTHING)  # 博客分类，外键
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # 作者,外键
    created_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    last_update_time = models.DateTimeField(auto_now=True)  # 最后一次修改时间

    def __str__(self):
        return '<Blog: %s>' % self.title

    class Meta:
        ordering = ['-created_time']  # 创建时间倒序排序


# class ReadNum(models.Model):
#     read_num = models.IntegerField(default=0)  # 阅读数
#     blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING)  # 一对一关联博客
