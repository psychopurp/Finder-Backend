"""
整个项目的url映射
"""
import django.contrib.admin as django_admin
from django.urls import path, re_path
from django.views.static import serve
from activity.urls import ACTIVITY_URL
from address.urls import ADDRESS_URL
from topic.urls import TOPIC_URL
from recommend.urls import RECOMMEND_URL
from user.urls import USER_URL
from project import settings

django_admin.autodiscover()

# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = \
    [
        path('admin/', django_admin.site.urls),
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve,
                {'document_root': settings.STATIC_ROOT_PATH}),
    ] + ADDRESS_URL + ACTIVITY_URL + TOPIC_URL + RECOMMEND_URL + USER_URL
