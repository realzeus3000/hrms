from django.shortcuts import render
from . models import Announcement


def index(request):
    announcements = Announcement.objects.all()
    context = {'announcements': announcements}
    return render (request, 'home/index.html', context)
