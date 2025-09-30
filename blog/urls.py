from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView
from .views import *

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('logout/', logout_view, name='logout'), 
]
