from django.shortcuts import render


def index(request):
    return render(request, 'blogs.html')


def recent(request):
    return render(request, 'blogs.html')
