from django.db import models

# Create your models here.
class Info(models.Model):
    name_kr = models.CharField(max_length = 10)
    name_eng = models.CharField(max_length = 20)
    email = models.CharField(max_length = 100)
    location = models.CharField(max_length = 30)
    career = models.TextField(default="현재 경력 사항이 없습니다.")
    sophomore = models.TextField(default="현재 학력 사항이 없습니다.")
    cert = models.TextField(default="현재 자격증 사항이 없습니다.")
    skill = models.TextField(default="현재 기술 사항이 없습니다.")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_kr

class Video(models.Model):
    video_title = models.CharField(max_length = 50)
    video_key = models.CharField(max_length = 30, default="")
    video_content = models.TextField(default="")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.video_title
