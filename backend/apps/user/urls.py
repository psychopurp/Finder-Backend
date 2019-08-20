from django.urls import path
from user.views import get_user_profile, modify_profile, upload_image, login

USER_URL = [
    path('api/get_user_profile/', get_user_profile, name='get_user_profile'),
    path('api/modify_profile/', modify_profile, name='modify_profile'),
    path('api/upload_image/', upload_image, name='upload_image'),
    path('api/login/', login, name='login')
]
