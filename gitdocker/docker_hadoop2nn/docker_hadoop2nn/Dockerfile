FROM centos
MAINTAINER tsunx drill_chen@foxmail.com

ENV BUILD_ON 2018-11-30

COPY configs /tmp

RUN yum install -y  net-tools wget which openssh-clients openssh-server openssl-server
RUN yum install -y  gcc  gcc-c++  make  tar  openssl  openssl-devel  cmake


#DAEMONIZE
ADD ./daemonize.tar.gz  /usr/local

#JDK
ADD ./jdk-8u161-linux-x64.tar.gz  /usr/local/lib

#HADOOP
ADD ./hadoop-2.6.5.tar.gz  /usr/local

#ZOOKEEPER
ADD ./zookeeper-3.4.10.tar.gz  /usr/local


ENV JAVA_HOME    /usr/local/lib/jdk1.8.0_161

ENV HADOOP_HOME    /usr/local/hadoop-2.6.5

ENV ZOOKEEPER_HOME    /usr/local/zookeeper

ENV PATH    $PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$ZOOKEEPER_HOME


RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 600 ~/.ssh/authorized_keys

RUN cd  /usr/local/daemonize; ./configure; make -j 4; make install


RUN ln -s /usr/local/hadoop-2.6.5    /usr/local/hadoop
RUN ln -s /usr/local/zookeeper-3.4.10   /usr/local/zookeeper

RUN cd    /usr/local/hadoop-2.6.5

RUN mkdir -pv  /root/bigdata
RUN mkdir -pv  /usr/local/hadoop-2.6.5/databasket



RUN mv /tmp/core-site.xml    /usr/local/hadoop-2.6.5/etc/hadoop/core-site.xml  && \
    mv /tmp/hdfs-site.xml    /usr/local/hadoop-2.6.5/etc/hadoop/hdfs-site.xml  && \
    mv /tmp/slaves    /usr/local/hadoop-2.6.5/etc/hadoop/slaves  && \
    mv /tmp/yarn-site.xml    /usr/local/hadoop-2.6.5/etc/hadoop/yarn-site.xml  && \
    mv /tmp/pre-source    ~/pre-source  && \
    mv /tmp/start-test.sh    ~/start-test.sh


RUN source ~/.bash_profile

#limits

#sysctl

#transparent_hugepage


RUN echo $HADOOP_HOME
##RUN daemonize
RUN echo $JAVA_HOME
##RUN $JAVA_HOME/bin  -version



WORKDIR /root

CMD ["/bin/bash"]


