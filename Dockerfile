# 继承于
FROM ubuntu:17.04
# 安装redis
RUN apt-get update
RUN apt-get -y install redis-server
# 暴露端口
EXPOSE 6379

# 覆盖默认的容器启动指令
ENTRYPOINT  ["/usr/bin/redis-server"]
