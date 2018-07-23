from django.shortcuts import render
from django.http import HttpResponse


def index(request):
   return render (request, 'home/index.html')


# def index (request):
#     return HttpResponse('<h1>This is the index page</h1>')
