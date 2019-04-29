FROM python:3.6
#基于python3.6镜像
MAINTAINER lz1998 875543533@qq.com
#作者信息

RUN git clone https://github.com/lz1998/django-wca.git
#下载django项目

RUN pip install -r /django-wca/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
#从阿里云镜像安装django所需模块

EXPOSE 80
#开放80端口

CMD python /django-wca/manage.py runserver 0.0.0.0:80