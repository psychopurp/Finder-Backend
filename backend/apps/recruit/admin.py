from django.contrib import admin
from recruit.models import RecruitType, Recruit, Candidate

# Register your models here.
admin.site.register(RecruitType)
admin.site.register(Recruit)
admin.site.register(Candidate)
