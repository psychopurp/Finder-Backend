'''
推荐的模型
'''
from django.db import models
# Create your models here.
class Recommend(models.model):
    image = models.CharField()
    location = models.CharField()
    class Meta:
        verbose_name = '推荐轮图'
        verbose_name_plural = verbose_name