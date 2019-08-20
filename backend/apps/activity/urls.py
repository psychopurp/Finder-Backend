from django.urls import path
from activity.views import get_activities, add_activity

ACTIVITY_URL = [
    path('api/get_activities/', get_activities, name='get_activities'),
    path('api/add_activity/', add_activity, name='add_activity')
]
