FROM centos
MAINTAINER tsunx drill_chen@foxmail.com

ENV BUILD_ON 2018-11-21

COPY configs /tmp

RUN yum install -y  net-tools wget which openssh-clients openssh-server openssl-server
RUN yum install -y  gcc  gcc-c++  make  tar  openssl  openssl-devel  cmake


#REDIS
ADD ./redis-4.0.9.tar.gz  /usr/local


ENV REDIS_HOME     /data/redis

ENV PATH    $PATH:$REDIS_HOME/bin

RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 600 ~/.ssh/authorized_keys

RUN cd  /usr/local/redis-4.0.9; make

RUN mkdir -pv  /data/redis/bin  /data/redis/conf

RUN cp  /usr/local/redis-4.0.9/src/redis-*  /data/redis/bin
RUN rm  /data/redis/bin/*.c   /data/redis/bin/*.o


RUN ln -s  /data/redis/bin/redis-server  /usr/local/bin/redis-server
RUN ln -s  /data/redis/bin/redis-cli     /usr/local/bin/redis-cli

RUN mv /tmp/redis.conf     /data/redis/conf/redis.conf && \
    mv /tmp/init_redis.sh  ~/init_redis.sh

RUN source ~/.bash_profile

#limits

#sysctl

#transparent_hugepage


RUN echo $REDIS_HOME
RUN redis-cli  --version

#/data/redis/bin/redis-server  /data/redis/conf/redis.conf

WORKDIR /root

CMD ["/bin/bash"]


