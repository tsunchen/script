echo start prometheus container...
docker run -itd --restart=always --net=host \
                --privileged \
                --name dkr_prometheus_run \
                --hostname prometheus-run \
                dkr_prometheus  /usr/sbin/init



echo start sshd...
docker exec -it dkr_prometheus systemctl start sshd




echo finished
docker ps

