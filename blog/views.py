from django.shortcuts import render, redirect
from .models import Post
from .forms import FormPost
# Create your views here.

def all_posts(request):
    data = Post.objects.all()
    
    return render(request, 'all_posts.html', {'posts': data})


def single_post(request, post_id):
    data = Post.objects.get(id= post_id)
    return render(request, 'single_post.html', {'post': data})

def new_post(request):
    # Check if send data
    if request.method == 'POST':
        # Get data from html
        form = FormPost(request.POST, request.FILES)
        if form.is_valid():
            # Save data without sending to model
            myForm = form.save(commit= False)
            # Choose the current user
            myForm.author = request.user
            myForm.save()
            return redirect('/blog')

    else:
        form = FormPost()

    return render(request, 'new_post.html', {'form': form})

def edit_post(request, post_id):
    # Get data and use it inside form
    data = Post.objects.get(id= post_id)
    if request.method == 'POST':
        # Fill data in fields
        form = FormPost(request.POST, request.FILES, instance=data)
        if form.is_valid():
            myForm = form.save(commit= False)
            myForm.author = request.user
            myForm.save()
            return redirect('/blog')
    else:
        form = FormPost(instance= data)

    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, post_id):
    data = Post.objects.get(id =post_id)
    data.delete()
    return redirect('/blog')


