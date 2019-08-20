from django.urls import path
from topic.views import get_topics, get_topic_comments, add_topic_comment

TOPIC_URL = [
    path('api/get_topics/', get_topics, name='get_topics'),
    path('api/get_topic_comments/', get_topic_comments, name='get_topic_comments'),
    path('api/add_topic_comment/', add_topic_comment, name='add_topic_comment')
]
