"""
整个项目的url映射
"""
import django.contrib.admin as django_admin
from django.urls import path, re_path
from django.views.static import serve

from project import settings

django_admin.autodiscover()

# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = \
    [
        path('index/', index, name='index_page'),
        path('admin/', django_admin.site.urls),
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve,
                {'document_root': settings.STATIC_ROOT_PATH}),
    ]