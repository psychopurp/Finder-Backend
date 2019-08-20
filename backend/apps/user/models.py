"""
用户的模型
"""
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from address.models import Major, School


class UserProfile(AbstractUser):
    """
    使用AbstractUser中的username作为uuid,
    使用AbstractUser中的password, 经过sha256加密
    AbstractUser提供date_joined作为注册时间
    AbstractUser提供is_staff作为是否为管理员
    AbstractUser提供status判断用户状态
    """
    nickname = models.CharField(max_length=40, blank=True, null=True, verbose_name='昵称')
    phone = models.CharField(max_length=11, unique=True, verbose_name='电话')
    avatar = models.CharField(max_length=128, blank=True, null=True, verbose_name='头像')
    introduction = models.TextField(blank=True, null=True, verbose_name='自我介绍')
    birthday = models.DateField(verbose_name='出生日期', blank=True, null=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname if self.nickname else 'None'


class Login(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
    time = models.DateTimeField(default=datetime.now)