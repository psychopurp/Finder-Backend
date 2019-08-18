"""
记录项目中发生的一些异常情况
"""
import os
from datetime import datetime

from project.settings import BASE_DIR, OPEN_TIME


def log(*args, sep=' ', end='\n'):
    path = os.path.join(BASE_DIR, 'log')
    file_name = 'runtime_log' + str(OPEN_TIME) + '.log'
    if not os.path.exists(path):
        os.makedirs(path)
    now = datetime.now().strftime('[%Y-%m-%d %H:%S:%M]\t')
    with open(os.path.join(path, file_name), 'a') as log_file:
        log_file.write(now)
        for word in args:
            log_file.write(str(word))
            log_file.write(str(sep))
        log_file.write(str(end))
