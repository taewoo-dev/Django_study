from django.db import models


# Create your models here.
# 데이터베이스 스키마모델
class Post(models.Model):
    # 길이 제한 있음
    title = models.CharField(max_length=100)
    # 길이제한 없음
    content = models.TextField()
    tag_set = models.ManyToManyField("Tag", blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
