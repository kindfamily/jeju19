# from django.db import models
# from taggit.managers import TaggableManager

# class Cafe(models.Model):
#     name = models.CharField(max_length = 50)
#     lat = models.FloatField(null=True)
#     lng = models.FloatField(null=True)
#     mainphoto = models.ImageField(blank=True, null=True)
#     subphoto = models.ImageField(blank=True, null=True)
#     publishedDate = models.DateTimeField(blank=True, null=True)
#     modifiedDate = models.DateTimeField(blank=True, null=True)   # blank=True는 어드민 계정으로 접속했을 때 빈칸이 없어야 한다는 
#     content = models.TextField()
#     locate = models.TextField(null=True)
#     phone = models.TextField(null=True)
#     insta = models.TextField(null=True)
#     tag = TaggableManager(blank=True)   # tag 만 관리하는 라이브러리
    
#     def __str__(self):
#         return self.name


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

from django.db import models
from taggit.managers import TaggableManager

# 회원관리
class Member(models.Model):
    cate = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    mainphoto = models.ImageField(blank=True, null=True)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    password_confirm = models.CharField(max_length = 50)
    joinDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
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
class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    
    def __str__(self):
        return self.question

    
    
    
    
    
    
    
    
    
    
    
