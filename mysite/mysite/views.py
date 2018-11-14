from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World\nddd贺鹏程</br>真帅")
