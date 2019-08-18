# Finder Backend

## 简介

Finder Backend

## 使用流程

1. 检查环境, 要求存在docker和docker-compose.
2. `docker-compose build` 执行此命令将建构运行进行.
3. `docker-compose run backend python manage.py makemigrations ` 执行此命令生产数据库迁移文件.
4.  `docker-compose run backend python manage.py migrate ` 生成数据表.
5. `docker-compose run backend python manage.py createsuperuser` 首次运行要求必须存在一个超级用户
6. `docker-compose up` 完成运行, 接下来, 打开 http://127.0.0.1:8000 , 即可体验本项目!

在之后的运行中, 只需要在backend的目录下, 运行`docker-compose up`, 即可运行并体验本项目.



### 其他操作

Django生成数据表:

- 此操作一般不需要执行

  - `docker-compose run backend python manage.py migrate`

Docker Createsuperuser:

- 需要新建超级用户时需要执行此操作.

  - `docker-compose run backend python manage.py createsuperuser`

lint命令:

- 如需执行pylint, 可使用此命令.
- `docker-compose run backend pylint --rcfile=.pylintrc apps project`