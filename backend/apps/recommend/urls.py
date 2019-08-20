from django.urls import path
from recommend.views import get_recommend

RECOMMEND_URL = [
    path('api/get_recommend/', get_recommend, name='get_recommend')
]
