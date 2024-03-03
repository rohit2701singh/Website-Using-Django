from django.urls import path
from . import views     # from django_project.blog import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView


urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('about/', views.about, name="blog-about"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),   #<pk> primary key id
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),   
]


# <app>/<model>_<viewtype>.html this is where PostListView looking for template--> blog/post_list.html