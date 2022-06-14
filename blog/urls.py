from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.youn),
    path('post_list/', views.post_list),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), 
]
