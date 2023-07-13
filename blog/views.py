from django.shortcuts import render
from .models import Post
# Create your views here.

def all_posts(request):
    data = Post.objects.all()
    
    return render(request, 'all_posts.html', {'posts': data})