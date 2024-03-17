from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
import sweetify
# Create your views here.

def index_view(request):
    return render (request, 'website/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request,'submited successfully!')
            return HttpResponseRedirect('/')
        else:
            sweetify.error(request, 'submit failed!')
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
        return render (request, 'website/contact.html')

def about_view(request):
    return render (request, 'website/about.html')