"""
用户相关中间件. 主要包括登录中间件.
"""
import time

from django.http import HttpRequest
from django.utils.deprecation import MiddlewareMixin

from user.models import Login


class LoginMiddleWare(MiddlewareMixin):
    TIMEOUT = 3600 * 24

    def process_request(self, request: HttpRequest):
        token = request.headers.get('Token')
        login = Login.objects.filter(token=token)
        if login and time.time() - login[0].time.timestamp() < self.TIMEOUT:
            request.user = login[0].user
        else:
            request.user = None
