from django.urls import path, include
from . import views

urlpatterns = [
    path('/', views.youn),
    path('post_list/', views.post_list),
]
