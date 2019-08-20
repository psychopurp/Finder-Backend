"""
地区相关模型
"""
from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=200, verbose_name='省份', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '省份'
        verbose_name_plural = verbose_name


class City(models.Model):
    name = models.CharField(max_length=200, verbose_name='市', unique=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=200, verbose_name='学校', unique=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    introduction = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学校'
        verbose_name_plural = verbose_name


class Major(models.Model):
    """
    专业, 不同学校可以有相同的专业, 所以没有直接引用学校
    """
    name = models.CharField(max_length=200, unique=True)
    introduction = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '专业'
        verbose_name_plural = verbose_name
