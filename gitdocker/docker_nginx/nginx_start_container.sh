echo start nginx container...
docker run -itd --restart=always --net=host \
                --privileged \
                --name dkr_nginx_run \
                --hostname nginx-run \
                dkr_nginx  /usr/sbin/init



echo start sshd...
docker exec -it dkr_nginx systemctl start sshd




echo finished
docker ps

