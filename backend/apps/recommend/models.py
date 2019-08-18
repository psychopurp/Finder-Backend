"""
推荐的模型
"""
from django.db import models


# Create your models here.
class Recommend(models.Model):
    image = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    class Meta:
        verbose_name = '推荐轮图'
        verbose_name_plural = verbose_name
