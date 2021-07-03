from django.shortcuts import render
from .models import Post

def blog_index(request):
    posts = Post.objects.all()
    return render(request, 'blog_index.html', {'posts': posts})

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'post': post})

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)