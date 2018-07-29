from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('add/', views.add_post, name='post_added'),
    path('post/<slug:slug>/', views.posts, name='post_detail'),
]
