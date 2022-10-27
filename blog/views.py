# VIEWS BLOG
from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    data = Post.objects.all()
    context = {
        'title': 'Blog',
        'heading': 'Blog',
        'subheading': 'Postingan',
        'post': data
    }
    return render(request, 'blog/index.html',context=context)
