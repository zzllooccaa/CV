from django.shortcuts import render, get_object_or_404
from .models import Blog
from .getip import get_client_ip


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})


def games(request):
    ipaddress = get_client_ip(request)
    return render(request, 'blog/games.html',{'blog': ipaddress})
