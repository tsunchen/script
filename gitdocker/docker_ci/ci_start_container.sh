echo start ci container...
docker run -itd --restart=always --net=host \
                --privileged \
                --name dkr_ci_run \
                --hostname ci-run \
                dkr_ci  /usr/sbin/init



echo start sshd...
docker exec -it dkr_ci_run systemctl start sshd




echo finished
docker ps

