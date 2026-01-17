from django.shortcuts import render, redirect
from .models import Post
from datetime import date
from .forms import PostForm
from django.contrib.auth.decorators import login_required

all_posts = [
    {'title': 'First Post', 'content': 'This is the content of the first post.'},
    {'title': 'Second Post', 'content': 'This is the content of the second post.'},
]


@login_required
def posts_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'posts_list.html', {'posts': posts})


# Create your views here.
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # create a Post object but don't save to the db yet
            post.created_at = date.today()
            post.save() # save on the db
            return redirect('posts_list')
        else:
            print(form.errors)
    else:
        form = PostForm()   
    return render(request, 'create_post.html', {'form': form})


@login_required
def edit_post(request, post_id):
    # get the post object to edit by its id
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
        else:
            print(form.errors)
    else:
        form = PostForm(instance=post)   
    return render(request, 'edit_post.html', {'form': form, 'post': post})


@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    
    if(request.method == 'POST'):
        post.delete()
        
    return redirect('posts_list')


