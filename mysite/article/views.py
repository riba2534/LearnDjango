from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def article_detail(request, article_id):
    return HttpResponse("文章id: %s" % article_id)
