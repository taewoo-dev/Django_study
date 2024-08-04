from django.db import models


# Create your models here.
# 데이터베이스 스키마모델
class Post(models.Model):
    # 길이 제한 있음
    title = models.CharField(max_length=100)
    # 길이제한 없음
    content = models.TextField()
