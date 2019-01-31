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

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})

    
# 자동생성 폼 입력 모듈 클래스
# from django.db import models
# from taggit.managers import TaggableManager

# class Cafe(models.Model):
#     name = models.CharField(max_length = 50)
#     lat = models.FloatField(null=True)
#     lng = models.FloatField(null=True)
#     mainphoto = models.ImageField(blank=True, null=True)
#     subphoto = models.ImageField(blank=True, null=True)
#     content = models.TextField()
#     publishedDate = models.DateTimeField(blank=True, null=True)
#     modifiedDate = models.DateTimeField(blank=True, null=True)
#     tag = TaggableManager(blank=True)
#     locate = models.TextField(null=True)
#     phone = models.TextField(null=True)
#     insta = models.TextField(null=True)

#     def __str__(self):
#         return self.name


# 홈앤홈

# from django.db import models
# from taggit.managers import TaggableManager

# # 회원관리
# class Member(models.Model):
#     cate = models.CharField(max_length = 50)
#     name = models.CharField(max_length = 50)
#     mainphoto = models.ImageField(blank=True, null=True)
#     email = models.CharField(max_length = 50)
#     password = models.CharField(max_length = 50)
#     password_confirm = models.CharField(max_length = 50)
#     joinDate = models.DateTimeField(blank=True, null=True)

#     def __str__(self):
#         return self.name
    
# FAQ
# class Faq(models.Model):
#     cate = models.CharField(max_length = 50)
#     name = models.CharField(max_length = 50)
#     email = models.CharField(max_length = 50)
#     password = models.CharField(max_length = 50)
#     password_confirm = models.CharField(max_length = 50)
#     joinDate = models.DateTimeField(blank=True, null=True)

#     def __str__(self):
#         return self.name

    
    
# FAQ
# 넘버 | 질문 | 답변 | 
# 회원관리
# class Faq(models.Model):
#     question = models.TextField()
#     answer = models.TextField()
    
#     def __str__(self):
#         return self.question

    
    
    
    
    
    
    
    
    
    
    
