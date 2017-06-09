from django.shortcuts import render
from django.core.urlresolvers import reverse

def home(request):
    return render(request,'blog/home.html')

def info(request):
    return render(request,'blog/info.html')

def portfolio(request):
    return render(request,'blog/portfolio.html')

def video(request):
    return render(request,'blog/video.html')

def contact(request):
    return render(request,'blog/contact.html')
