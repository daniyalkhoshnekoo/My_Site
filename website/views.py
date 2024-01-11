from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse('hello world')

def contact_view(request):
    return HttpResponse('<h1>Contact page</h1>')

def about_view(request):
    return HttpResponse('<h1>About page</h1>')
