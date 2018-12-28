FROM centos
MAINTAINER tsunx drill_chen@foxmail.com

ENV BUILD_ON 2018-Dec-08

COPY configs /tmp


RUN yum install -y  net-tools wget which openssh-clients openssh-server
RUN yum install -y  gcc  gcc-c++  make  tar  openssl  openssl-devel  cmake  
#RUN yum install -y  ncurses  ncurses-devel
#RUN yum install -y  perl-Module-Install

RUN yum install -y epel-release
RUN yum install -y nagios-plugins*  nrpe


#PUSHGATEWAY
#ADD ./pushgateway-0.6.0.linux-amd64.tar.gz  /usr/local

#DAEMONIZE
#ADD ./daemonize.tar.gz  /usr/local

#MYSQL
#ADD ./mysql-5.6.39.tar.gz  /usr/local


#ENV MYSQL_HOME     /usr/local/mysql

#ENV PATH    $PATH:$MYSQL_HOME/bin

RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 600 ~/.ssh/authorized_keys

#RUN ln -s /usr/local/pushgateway-0.6.0.linux-amd64   /usr/local/pushgateway

#RUN cd  /usr/local/daemonize; ./configure; make; make install

#RUN cd  /usr/local/mysql-5.6.39; cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql  -DMYSQL_DATADIR=/data/mysql -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DWITH_EXTRA_CHARSETS:STRING=all -DWITH_DEBUG=0 -DWITH_SSL=yes -DWITH_READLINE=1 -DENABLED_LOCAL_INFILE=1; make; make install


#RUN mkdir -pv  /data/mysql


RUN mv /tmp/init_nrpe.sh     ~/init_nrpe.sh  && \
    mv /tmp/test_nrpe.sh  ~/test_nrpe.sh  && \
    mv /tmp/check_wait_connect  /usr/lib64/nagios/plugins/lcgdm/check_wait_connect  
#    mv /tmp/start-pushgateway.sh  ~/start-pushgateway.sh  && \
#    mv /tmp/my.cnf  /etc/my.cnf


RUN source ~/.bash_profile

#limits

#sysctl

#transparent_hugepage


#RUN echo $MYSQL_HOME
##RUN daemonize    -v
#RUN mysql   --version
#RUN /usr/local/pushgateway/pushgateway  --version

#RUN groupadd mysql
#RUN useradd -g mysql -M -s /sbin/nologin mysql
#RUN chown -R mysql:mysql  /usr/local/mysql
#RUN chown -R mysql:mysql  /data/mysql

WORKDIR /root

CMD ["/bin/bash"]


