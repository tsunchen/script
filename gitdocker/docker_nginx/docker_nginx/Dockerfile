FROM centos
MAINTAINER tsunx drill_chen@foxmail.com

ENV BUILD_ON 2018-11-28

COPY configs /tmp

RUN yum install -y  net-tools wget which openssh-clients openssh-server openssl-server
RUN yum install -y  gcc  gcc-c++  make  tar  openssl  openssl-devel  cmake


#DAEMONIZE
ADD ./daemonize.tar.gz  /usr/local

#NGINX
ADD ./nginx-1.12.1.tar.gz  /usr/local

#PUSHGATEWAY
ADD ./pushgateway-0.6.0.linux-amd64.tar.gz  /usr/local


ENV NGINX_HOME     /usr/local/nginx

ENV PATH    $PATH:$NGINX_HOME

RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 600 ~/.ssh/authorized_keys

RUN cd  /usr/local/daemonize; ./configure; make -j 4; make install
RUN cd  /usr/local/nginx-1.12.1; ./configure --prefix=/usr/local/nginx  --with-http_ssl_module --with-stream --with-stream_ssl_module; make -j 4; make install


RUN ln -s /usr/local/nginx    /usr/local/nginx
RUN ln -s /usr/local/pushgateway-0.6.0.linux-amd64   /usr/local/pushgateway

RUN cd    /usr/local/nginx

RUN mkdir -pv  /data/nginx



RUN mv /tmp/nginx.conf.template     /usr/local/nginx.conf.template  && \
    mv /tmp/start-nginx.sh  ~/start-nginx.sh && \
    mv /tmp/start-pushgateway.sh  ~/start-pushgateway.sh


RUN source ~/.bash_profile

#limits

#sysctl

#transparent_hugepage


RUN echo $NGINX_HOME
#RUN daemonize    --version
RUN /usr/local/nginx/sbin/nginx -V
RUN /usr/local/pushgateway/pushgateway  --version



WORKDIR /root

CMD ["/bin/bash"]


