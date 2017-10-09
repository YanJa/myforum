FROM python:3.5
# 环境变量
ENV PYTHONUNBUFFERED 1
# 创建目录
RUN mkdir /code
# 设置工作目录
WORKDIR /code
# 添加requirements.txt文件
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install uwsgi
ADD . /code/
