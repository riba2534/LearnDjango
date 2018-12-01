from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator  # 引入分页器
from .models import Blog, BlogType
from django.conf import settings


def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(
        blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)  # 每10页进行分页
    page_num = request.GET.get('page', 1)  # get获取page的参数
    page_of_blogs = paginator.get_page(page_num)  # 防止出错，防止用户瞎输
    current_page_num = page_of_blogs.number  # 获得当前页码
    # 当前页码前后两页
    page_range = list(range(max(current_page_num-2, 1), current_page_num)) + \
        list(range(current_page_num, min(current_page_num+2, paginator.num_pages)+1))
    # 加省略号
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages-page_range[-1] >= 2:
        page_range.append('...')
    # 加首尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    context['blog_dates'] = Blog.objects.dates(
        'created_time', 'month', order='DESC')
    return context


def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request, blogs_all_list)
    return render_to_response("blog/blog_list.html", context)


def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, id=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type
    return render_to_response("blog/blogs_with_type.html", context)


def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(
        created_time__year=year, created_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = '%s年%s月' % (year, month)
    return render_to_response("blog/blogs_with_date.html", context)


def blog_detail(request, blog_pk):  # 博客内容
    context = {}
    blog = get_object_or_404(Blog, pk=blog_pk)
    context['previous_blog'] = Blog.objects.filter(
        created_time__gt=blog.created_time).last()  # 找到当前博客的上一条
    context['next_blog'] = Blog.objects.filter(
        created_time__lt=blog.created_time).first()  # 找到当前博客的下一条
    context['blog'] = get_object_or_404(Blog, id=blog_pk)
    return render_to_response("blog/blog_detail.html", context)
