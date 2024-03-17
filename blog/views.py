from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponseRedirect

def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    paginator = Paginator(posts,3)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(1)

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

# def blog_category(request,cat_name):
#     posts = Post.objects.filter(status=1)
#     posts = posts.filter(category__name=cat_name)
#     context = {'posts': posts}
#     return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)


def test_view(request):
    return render(request, 'blog/test.html')

