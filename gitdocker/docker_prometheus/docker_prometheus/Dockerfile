FROM centos
MAINTAINER tsunx drill_chen@foxmail.com

ENV BUILD_ON 2018-11-22

COPY configs /tmp

RUN yum install -y  net-tools wget which openssh-clients openssh-server openssl-server
RUN yum install -y  gcc  gcc-c++  make  tar  openssl  openssl-devel  cmake


#DAEMONIZE
ADD ./daemonize.tar.gz  /usr/local

#PROMETHEUS
ADD ./prometheus-2.0.0.linux-amd64.tar.gz  /usr/local

#PUSHGATEWAY
ADD ./pushgateway-0.6.0.linux-amd64.tar.gz  /usr/local


ENV PROMETHEUS_HOME     /usr/local/prometheus

ENV PATH    $PATH:$PROMETHEUS_HOME

RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 600 ~/.ssh/authorized_keys

RUN cd  /usr/local/daemonize; ./configure; make; make install

RUN ln -s /usr/local/prometheus-2.0.0.linux-amd64    /usr/local/prometheus
RUN ln -s /usr/local/pushgateway-0.6.0.linux-amd64   /usr/local/pushgateway

RUN cd    /usr/local/prometheus

RUN mkdir -pv  /data/prometheus



RUN mv /tmp/prometheus.yml.template     /usr/local/prometheus/prometheus.yml.template  && \
    mv /tmp/start-prometheus.sh  ~/start-prometheus.sh && \
    mv /tmp/start-pushgateway.sh  ~/start-pushgateway.sh


RUN source ~/.bash_profile

#limits

#sysctl

#transparent_hugepage


RUN echo $PROMETHEUS_HOME
RUN daemonize    -v
RUN /usr/local/prometheus/prometheus   --version
RUN /usr/local/pushgateway/pushgateway  --version



WORKDIR /root

CMD ["/bin/bash"]


