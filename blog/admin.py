from django.contrib import admin
from .models import Info, Video

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('name_kr','name_eng','email','create_at','update_at')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_title','create_at','update_at')
