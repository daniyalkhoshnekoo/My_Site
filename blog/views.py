from django.shortcuts import render,get_object_or_404
from .models import *

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request,pid):
    post = get_object_or_404(Post, id=pid, status=1)
    post.counted_views += 1
    post.save()
    prev_post = Post.objects.filter(pk__lt=post.id).order_by('-id').first()
    next_post = Post.objects.filter(pk__gt=post.id).order_by('id').first()
    context = {
        'post':post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    return render(request, 'blog/blog-single.html', context)

def test_view(request):
    return render(request, 'blog/test.html')
