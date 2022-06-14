from django.urls import path, include
from . import views

urlpatterns = [
     path('/', views.youn, name='index'),
    path('/post_list', views.post_list, name='post_list'),
]
