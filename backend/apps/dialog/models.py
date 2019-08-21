from django.db import models
from user.models import UserProfile
from datetime import datetime


# Create your models here.
class Dialog(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now)
    content = models.TextField()

    class Meta:
        verbose_name = '聊天消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sender + '向' + self.receiver + '发送消息'
