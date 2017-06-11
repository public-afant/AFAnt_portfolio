from django.contrib import admin
from .models import Info

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('name_kr','name_eng','email','create_at','update_at')

