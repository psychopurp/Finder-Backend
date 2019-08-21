from django.db import models
from user.models import UserProfile
from datetime import datetime


# Create your models here.
class CandidateStatus:
    REJECT = 0
    WAITING = 1
    ACCEPT = 2



class Candidate(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now)
    information = models.TextField()
    status = models.IntegerField(
        choices=(
            (CandidateStatus.REJECT, '拒绝'), (CandidateStatus.WAITING, '等待'), (CandidateStatus.ACCEPT, '接受')
        ), default=CandidateStatus.WAITING
    )

    class Meta:
        verbose_name = '应聘者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user


class RecruitType(models.Model):
    name = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = '招募类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Recruit(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=100)
    introduction = models.TextField()
    candidates = models.ManyToManyField(Candidate)
    type = models.ManyToManyField(RecruitType)

    class Meta:
        verbose_name = '招募'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '招募:' + self.title
