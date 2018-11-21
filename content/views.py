from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.order_by('-date')
    return render(request,'content/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts = Post.objects.order_by('-date')
    comments = Comment.objects.filter(post_id=pk)
    return render(request, 'content/post_detail.html', {'post': post, 'posts':posts, 'comments':comments})

def about_me(request):
    posts = Post.objects.order_by('-date')
    return render(request, 'content/about_me.html', {'posts':posts})

def new_post(request):
    posts = Post.objects.order_by('-date')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'content/new_post.html', {'form':form,'posts':posts})


def edit_post(request, pk):
    posts = Post.objects.order_by('-date')
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'content/new_post.html', {'form':form, 'posts':posts})

def new_comment(request, pk):
    posts = Post.objects.order_by('-date')
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = pk
            comment.date = timezone.now()
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'content/new_comment.html',{'form':form, 'posts':posts})
