from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    data = {'admin': False, 'member': False}
    # return HttpResponse('Hello World')
    return render(request, 'myApp/index.html', data)


def about(request):
    return render(request, 'myApp/about.html')
