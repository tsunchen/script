#!/bin/bash

#limits
echo "*       -       nofile  10240" >> /etc/security/limits.conf
bash
ulimit -n


#sysctl
echo "net.core.somaxconn = 10240" >> /etc/sysctl.conf
echo "vm.overcommit_memory = 1" >> /etc/sysctl.conf
sysctl -p
sysctl -a | grep somaxconn
sysctl -a | grep commit_memory


#transparent_hugepage
echo never > /sys/kernel/mm/transparent_hugepage/enabled
cat /sys/kernel/mm/transparent_hugepage/enabled


