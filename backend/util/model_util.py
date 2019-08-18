"""
模型相关转换工具
"""
import random
import time


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
        for key in result_dict:
            if key.startswith("_"):
                del result_dict[key]
        return result_dict
    result_dict = {}
    for prop in props:
        if isinstance(prop, str):
            result_dict[prop] = model.__getattribute__(prop)
        elif isinstance(prop, type(get_time)):
            result_dict[prop[0]] = prop[1](model.__getattribute__(prop[0]))
        else:
            result_dict[prop[0]] = model.__getattribute__(prop[0]).__getattribute__(prop[1])()
    return result_dict


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


def generate_random_str(length=32):
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
