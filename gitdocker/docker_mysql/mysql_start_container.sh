echo start zabbix container...
docker run -itd --restart=always --net=host \
                --privileged \
                --name dkr_zabbix_run \
                --hostname zabbix-run \
                dkr_zabbix  /usr/sbin/init



echo start sshd...
docker exec -it dkr_zabbix systemctl start sshd




echo finished
docker ps

