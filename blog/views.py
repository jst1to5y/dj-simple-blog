from django.shortcuts import render
from .models import Post
# Create your views here.

def all_posts(request):
    data = Post.objects.all()
    
    return render(request, 'all_posts.html', {'posts': data})


def single_post(request, post_id):
    data = Post.objects.get(id= post_id)
    return render(request, 'single_post.html', {'post': data})