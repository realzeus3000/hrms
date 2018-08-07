from django.urls import path
from . import views

urlpatterns = [
    path('list_paths/', views.list_path, name='listpaths' ),
    path('add_paths/', views.add_paths, name='addpaths'),
]
