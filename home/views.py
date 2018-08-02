from django.shortcuts import render, redirect
from . models import Announcement
from . import forms
from django.http import HttpResponse

def index(request):
    announcements = Announcement.objects.all().order_by('-create')
    context = {'announcements': announcements}
    return render (request, 'home/index.html', context)

def add_post(request):
    if request.method == 'POST':
        form = forms.AddPost(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.AddPost()
    context = {'form': form}
    return render(request,'home/add_post.html', context )


def posts(request, slug):
    post = Announcement.objects.get(slug=slug)
    context ={
    'post': post
    }
    return render(request, 'home/post_review.html', context)
    # return HttpResponse(slug)
