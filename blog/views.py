from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Info, Video, Dev

def home(request):
    return render(request,'blog/home.html')

def info(request):
    info_list = Info.objects.all()
    return render(request,'blog/info.html',{'info_list': info_list})

def portfolio(request):
    dev_list = Dev.objects.all()
    return render(request,'blog/portfolio.html',{'dev_list' : dev_list})

def video(request):
    video_order_by = Video.objects.all()
    video_list = video_order_by.order_by('-create_at')
    return render(request,'blog/video.html',{'video_list' : video_list})

def contact(request):
    info_list = Info.objects.all()
    return render(request,'blog/contact.html',{'info_list' : info_list})
