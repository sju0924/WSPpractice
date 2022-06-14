import imp
from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_data')
    return render(request, 'blog/post_list.html', {'posts': posts})
def youn(request):
    return render(request, 'blog/youn.html', {})
