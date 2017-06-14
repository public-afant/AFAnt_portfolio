from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Info, Video

def home(request):
    return render(request,'blog/home.html')

def info(request):
    info_list = Info.objects.all()
    return render(request,'blog/info.html',{'info_list': info_list})

def portfolio(request):
    return render(request,'blog/portfolio.html')

def video(request):
    video_order_by = Video.objects.all()
    video_list = video_order_by.order_by('-create_at')
    return render(request,'blog/video.html',{'video_list' : video_list})

def contact(request):
    info_list = Info.objects.all()
    return render(request,'blog/contact.html',{'info_list' : info_list})
