"""
登录检查相关装饰器
"""
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest, JsonResponse

from error import ErrorInformation

from util.log_util import log


# 登录装饰器
def login_require(func):
    def wrapper(request: HttpRequest, *args, **kwargs):
        if not request.user or isinstance(request.user,
                                          AnonymousUser) or not request.user.is_active:
            # 如果没有登录
            log("error:", request.user)
            return JsonResponse({'status': False, 'error': ErrorInformation.login_require})
        log("success:", request.user)
        return func(request, *args, **kwargs)

    return wrapper