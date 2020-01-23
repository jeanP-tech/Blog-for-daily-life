from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image
import re

from django.contrib import auth

def index(request):
    return render(request, 'blog/index.html', {})

def post_list(request):
    post_list = Post.objects.order_by('-created_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post.html', {'post_list':post_list, 'page_obj':page_obj})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def reject(request):
    return render(request, 'blog/reject.html')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def art(request):
    return render(request, 'blog/paint.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"]
            )
            auth.login(request, user)
            return redirect('index')
        return render(request, "blog/signup.html")
    return render(request, 'blog/signup.html')

def login(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'blog/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'blog/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
