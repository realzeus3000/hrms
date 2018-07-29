from django.shortcuts import render
from . models import Announcement
# from . forms import AddPost
from django.http import HttpResponse

def index(request):
    announcements = Announcement.objects.all().order_by('-create')
    context = {'announcements': announcements}
    return render (request, 'home/index.html', context)

# def add_post(request):
#     forms = AddPost()
#     if form.is_valid():
#         new_form = form
#
#     context = {
#     'form' : form
#     }
#     return render(request, 'home/add_post.html', context)


def posts(request, slug):
    post = Announcement.objects.get(slug=slug)
    context ={
    'post': post
    }
    return render(request, 'home/post_review.html', context)
    # return HttpResponse(slug)
