from django.contrib import admin
from .models import Topic, TopicComment
# Register your models here.
admin.site.register(TopicComment)
admin.site.register(Topic)
