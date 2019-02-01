from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse


# 기존 cafe 입력 폼 

class Cafe(models.Model):
    이름 = models.CharField(max_length = 50)
    위도 = models.FloatField(null=True)
    경도 = models.FloatField(null=True)
    메인사진 = models.ImageField(blank=True, null=True)
    서브사진 = models.ImageField(blank=True, null=True)
    publishedDate = models.DateTimeField(blank=True, null=True)
    modifiedDate = models.DateTimeField(blank=True, null=True)   # blank=True는 어드민 계정으로 접속했을 때 빈칸이 없어야 한다는 
    소개 = models.TextField()
    위치 = models.TextField(null=True)
    전화 = models.TextField(null=True)
    인스타 = models.TextField(null=True)
    tag = TaggableManager(blank=True)   # tag 만 관리하는 라이브러리
    
    def __str__(self):
        return self.이름