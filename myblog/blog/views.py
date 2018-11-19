from django.shortcuts import render_to_response, get_object_or_404
from .models import *


def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    context['blog_types'] = BlogType.objects.all()
    return render_to_response("blog/blog_list.html", context)


def blog_detail(request, blog_pk):  # 博客内容
    context = {}
    context['blog'] = get_object_or_404(Blog, id=blog_pk)
    return render_to_response("blog/blog_detail.html", context)


def blogs_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, id=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()
    return render_to_response("blog/blogs_with_type.html", context)
