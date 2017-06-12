from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Info

def home(request):
    return render(request,'blog/home.html')

def info(request):
    info_list = Info.objects.all()
    return render(request,'blog/info.html',{'info_list': info_list})

def portfolio(request):
    return render(request,'blog/portfolio.html')

def video(request):
    return render(request,'blog/video.html')

def contact(request):
    info_list = Info.objects.all()
    return render(request,'blog/contact.html',{'info_list' : info_list})
