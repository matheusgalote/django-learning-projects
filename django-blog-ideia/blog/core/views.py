from django.shortcuts import render
from .models import Post, Comment

def blog_index(request):
    post = Post.objects.all().order_by('-created_on')
    context = {
        'post': post
    }
    return render(request, 'blog_index.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)