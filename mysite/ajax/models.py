from django.db import models
from django.conf import settings

# Create your models here.
class Like(models.Model):
    이름 = models.CharField(max_length = 50)
    like_user_set = models.ManyToManyField('like', blank=True)

    def __str__(self):
        return self.이름