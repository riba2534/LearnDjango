from django.db import models
#from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    is_deleted = models.BooleanField(default=False)  # 文章是否被删除
    readed_num = models.IntegerField(default=0)# 阅读数量
    

    def __str__(self):
        return "<标题为: %s>" % self.title
