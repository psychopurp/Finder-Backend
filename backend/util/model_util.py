"""
模型相关转换工具
"""
import random
import time

from util.log_util import log


def get_time():
    return str(int(time.time()))


def model_to_dict(model, props=None) -> dict:
    """
    将一个model实例转换成dict
    :param model: 需要转换的模型实例
    :param props: 需要转换的字段, 不传将转换所有字段, 如需对某个字段特殊处理, 可传入方法或字符串.
            如, 需要把datetime字段转成时间戳, 请传[["time", "timeslot"]], 将自动调用datetime对象的timeslot方法,
            也可传入一个函数, 如需要对time字段调用int方法, 请传[["time", int]], 将自动调用int方法
    :return: 转换后的dict
    """
    if not props:
        result_dict = model.__dict__
        deletes = []
        for key in result_dict:
            if key.startswith("_"):
                deletes.append(key)
        for key in deletes:
            del result_dict[key]
        return result_dict
    result_dict = {}
    for prop in props:
        if isinstance(prop, str):
            result_dict[prop] = model.__getattribute__(prop)
        elif isinstance(prop[1], str):
            if isinstance(model.__getattribute__(prop[0]).__getattribute__(prop[1]), type(get_time)):
                result_dict[prop[0]] = model.__getattribute__(prop[0]).__getattribute__(prop[1])(*prop[2:])
            else:
                result_dict[prop[0]] = model.__getattribute__(prop[0]).__getattribute__(prop[1])
        else:
            result_dict[prop[0]] = prop[1](model.__getattribute__(prop[0]), *prop[2:])
    return result_dict


def get_result_by_query_page(model, query=None, page=0, props=None) -> dict:
    """
    可直接对模型获取并分页
    :param model: 需要获取的模型
    :param query: 需要获取的查询方法, 需要是一个Q对象
    :param page: 需要的页数
    :param props: 需要获取的字段, 遵循和model_to_dict同样规则
    :return: 返回获取的后的dict
    """
    if not query:
        data = model.objects.all()
    else:
        data = model.objects.filter(query)
    result, total_page = get_query_set_by_page(data, page)
    return {'data': query_set_to_list(result, props), 'total_page': total_page, 'status': True,
            'has_more': page * 10 < total_page}


def get_query_set_by_page(query, page: int, page_size: int = 10) -> (all, int):
    """
    获取分页后的query_set
    :param query: 待分页的序列
    :param page: 需要的页数
    :param page_size: 每一页的大小
    :return: 返回值第一个为分页后的结果, 第二个是总页数
    """
    page = int(page)
    total_page = len(query) / page_size
    if total_page % 1 > 0:
        # 如果未填满一页的条, 按一页算
        total_page += 1
    total_page = int(total_page)
    if page + 1 > total_page:
        # 如果页数过多, 返回空的queryset
        return query[0:0], total_page
        # 如果页数正常, 返回结果
    return query[page * page_size: (page + 1) * page_size], total_page


def query_set_to_list(query_set, props=None) -> list:
    """
    将query_set转换成dict组成的列表
    :param query_set: 需要转换的queryset
    :param props: 需要转换的字段, 不传将转换所有字段, 如需对某个字段特殊处理, 可传入方法或字符串.
            如, 需要把datetime字段转成时间戳, 请传[["time", "timeslot"]], 将自动调用datetime对象的timeslot方法,
            也可传入一个函数, 如需要对time字段调用int方法, 请传[["time", int]], 将自动调用int方法
    :return: 有转化后的dict组成的列表
    """
    if not len(query_set):
        return []
    return [model_to_dict(i, props) for i in query_set]


def generate_random_str(length=32) -> str:
    """
    生成随机字符串
    :param length: 字符串长度
    :return: 生成的字符串
    """
    str_token = []
    for char in range(ord('0'), ord('9') + 1):
        str_token.append(chr(char))
    for char in range(ord('a'), ord('z') + 1):
        str_token.append(chr(char))
    for char in range(ord('A'), ord('Z') + 1):
        str_token.append(chr(char))
    result_str = ""
    for _ in range(length):
        result_str += str_token[random.randint(0, len(str_token) - 1)]
    return result_str


def str_page_to_int(page: str) -> int:
    if not page:
        page = 0
    try:
        page = int(page)
    except TypeError:
        page = 0
    except ValueError:
        page = 0
    return page


def error_return(error):
    return {"status": True, "error": error}


def from_id_get_object(obj_id, obj):
    try:
        obj_id = int(obj_id)
    except TypeError as e:
        log(e)
        return None
    except ValueError as e:
        log(e)
        return None
    try:
        result = obj.objects.get(id=obj_id)
    except obj.DoesNotExist:
        return None
    return result
