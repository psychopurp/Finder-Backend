'''
活动的模型
'''
from django.db import models
from user.models import UserProfile


class ActivityCategory(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='类别名称')


class Activity(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    sponsor = models.CharField(max_length=128, verbose_name='主办方')
    title = models.CharField(max_length=128)
    place = models.CharField(max_length=128, verbose_name='地点')
    poster = models.CharField(max_length=128, verbose_name='海报')
    start_time = models.DateTimeField(verbose_name='开始时间')
    end_time = models.DateTimeField(verbose_name='结束时间')
    description = models.TextField(verbose_name='详细描述')
    categories = models.ManyToManyField(ActivityCategory)

    def __str__(self):
        return '活动' + self.title
