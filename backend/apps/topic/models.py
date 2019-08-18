"""
话题的模型
"""
from django.db import models
from datetime import datetime
from address.models import School
from user.models import UserProfile


class Topic(models.Model):
    """
    school为空则为校际话题，否则为校内话题
    """
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=128, null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = '话题'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.school:
            return '校内话题：' + self.title
        else:
            return '校际话题：' + self.title


class TopicComment(models.Model):
    """
    refer_comment为空则为评论，否则为回复
    """
    refer = models.ForeignKey(Topic, on_delete=models.CASCADE)
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    create_time = models.DateTimeField(default=datetime.now)
    refer_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = '话题评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.refer_comment:
            return self.sender + '回复了' + '话题（' + self.refer + ')'
        else:
            return self.sender + '评论了' + '话题（' + self.refer + ')'
