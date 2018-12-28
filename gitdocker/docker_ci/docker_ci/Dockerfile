FROM centos
MAINTAINER tsunx drill_chen@foxmail.com

ENV BUILD_ON 23-Dec-2018

COPY configs /tmp


RUN yum install -y  net-tools wget which openssh-clients openssh-server
RUN yum install -y  gcc  gcc-c++  make  tar  openssl  openssl-devel  cmake  
#RUN yum install -y  ncurses  ncurses-devel
#RUN yum install -y  perl-Module-Install
#RUN yum install -y epel-release

#JDK
ADD ./jdk-8u161-linux-x64.tar.gz  /usr/local/lib

#MAVEN
ADD ./apache-maven-3.6.0-bin.tar.gz  /usr/local

#TOMCAT
ADD ./apache-tomcat-8.5.37.tar.gz  /usr/local

#DAEMONIZE
ADD ./daemonize.tar.gz  /usr/local


ENV JAVA_HOME    /usr/local/lib/jdk1.8.0_161


ENV PATH    $PATH:$JAVA_HOME/bin

RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 600 ~/.ssh/authorized_keys



#RUN ln -s /usr/local/pushgateway-0.6.0.linux-amd64   /usr/local/pushgateway

RUN cd  /usr/local/daemonize; ./configure; make -j 2; make install

#RUN cd  /usr/local/mysql-5.6.39; cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql  -DMYSQL_DATADIR=/data/mysql -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DWITH_EXTRA_CHARSETS:STRING=all -DWITH_DEBUG=0 -DWITH_SSL=yes -DWITH_READLINE=1 -DENABLED_LOCAL_INFILE=1; make; make install


#RUN mkdir -pv  /data/mysql


RUN mv /tmp/jenkins.war     /usr/local/apache-tomcat-8.5.37/webapps/jenkins.war  && \ 
    mv /tmp/init_tomcat.sh  ~/init_tomcat.sh  && \
    mv /tmp/deploy.sh  ~/deploy.sh 
#    mv /tmp/init_elasticsearch.sh    ~/init_elasticsearch.sh  && \
#    mv /tmp/init_logstash.sh    ~/init_logstash.sh  && \
#    mv /tmp/logstash.conf  ~/logstash.conf
#    mv /tmp/check_wait_connect  /usr/lib64/nagios/plugins/lcgdm/check_wait_connect  
#    mv /tmp/start-pushgateway.sh  ~/start-pushgateway.sh  && \
#    mv /tmp/my.cnf  /etc/my.cnf


RUN source ~/.bash_profile

#limits

#sysctl

#transparent_hugepage


RUN useradd tomcat
RUN usermod -s /sbin/nologin tomcat
#RUN chown -R tomcat:tomcat  /usr/local/kibana-6.2.3-linux-x86_64/

##RUN daemonize    -v
#RUN /usr/local/pushgateway/pushgateway  --version

#RUN groupadd mysql
#RUN useradd -g mysql -M -s /sbin/nologin mysql

RUN echo $JAVA_HOME

WORKDIR /root

CMD ["/bin/bash"]


