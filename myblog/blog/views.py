from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator  # 引入分页器
from .models import Blog, BlogType


def blog_list(request):
    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list, 10)  # 每10页进行分页
    page_num = request.GET.get('page', 1)  # get获取page的参数
    page_of_blogs = paginator.get_page(page_num)  # 防止出错，防止用户瞎输

    context = {}
    context['page_of_blogs'] = page_of_blogs
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
