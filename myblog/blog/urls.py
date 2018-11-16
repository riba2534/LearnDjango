from django.urls import path
from . import views

# start with blog
urlpatterns = [
    path('<int:blog_pk>', views.blog_detail, name='blog_detail'),
    path('type/<int:blog_type_pk>', views.blogs_with_type, name='blogs_with_type'),

]
