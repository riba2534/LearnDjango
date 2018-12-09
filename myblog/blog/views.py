from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator  # 引入分页器
from .models import Blog, BlogType
from read_statistics.utils import read_statistics_once_read
from django.db.models import Count
from django.conf import settings
from django.contrib.contenttypes.models import ContentType


def get_blog_list_common_data(request, blogs_all_list):  # 为了代码复用
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

    # 获取日期对应的博客数量
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year,
                                         created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.annotate(
        blog_count=Count('blog'))  # 博客分类的对应博客数量,为什么小写?
    context['blog_dates'] = blog_dates_dict
    return context


def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request, blogs_all_list)
    return render(request, "blog/blog_list.html", context)


def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, id=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type
    return render(request, "blog/blogs_with_type.html", context)


def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(
        created_time__year=year, created_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = '%s年%s月' % (year, month)
    return render(request, "blog/blogs_with_date.html", context)


def blog_detail(request, blog_pk):  # 博客内容
    blog = get_object_or_404(Blog, pk=blog_pk)
    read_cookie_key = read_statistics_once_read(request, blog)
    context = {}
    context['previous_blog'] = Blog.objects.filter(
        created_time__gt=blog.created_time).last()  # 找到当前博客的上一条
    context['next_blog'] = Blog.objects.filter(
        created_time__lt=blog.created_time).first()  # 找到当前博客的下一条
    context['blog'] = get_object_or_404(Blog, id=blog_pk)
    response = render(request, "blog/blog_detail.html", context)  # 响应
    response.set_cookie(read_cookie_key, 'true')  # 设置cookie,有效期为浏览器关闭时
    return response
