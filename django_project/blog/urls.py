from django.urls import path
from . import views     # from django_project.blog import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
]

