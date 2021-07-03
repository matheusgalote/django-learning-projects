from django.shortcuts import render
from .models import Post

def blog_index(request):
    posts = Post.objects.all()
    return render(request, 'blog_index.html', {'posts': posts})