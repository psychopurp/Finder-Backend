"""
管理员权限登录装饰器
"""
from django.http import HttpRequest, JsonResponse

from error import ErrorInformation


def request_method_check(method_type):
    # 检查请求方法, 传入可以是字符串或列表, 支持一种类型直接传入支持的字符串, 支持多种类型传入列表
    # 调用形如@request_method_check('GET')
    def decorator(func):
        def wrapper(request: HttpRequest, *args, **kwargs):
            if isinstance(method_type, str) and request.method != method_type.upper():
                # 如果类型是字符串且不一致, 直接返回
                return JsonResponse({'status': False, 'error': ErrorInformation.request_error})
            if not isinstance(method_type, str) and request.method not in [i.upper() for i in
                                                                           method_type]:
                # 如果请求方法不在支持列表中, 返回
                return JsonResponse({'status': False, 'error': ErrorInformation.request_error})
            return func(request, *args, **kwargs)

        return wrapper

    return decorator


def no_request_arg(func):
    def wrapper(*args, **kwargs):
        args = args[1:]
        return func(*args, **kwargs)

    return wrapper
