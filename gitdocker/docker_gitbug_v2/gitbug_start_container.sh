echo start gitbug container...
docker run -itd --restart=always --net=host \
                --privileged \
                --name dkr_gitbug_run \
                --hostname gitbug-run \
                dkr_gitbug  /usr/sbin/init



echo start sshd...
docker exec -it dkr_gitbug_run systemctl start sshd




echo finished
docker ps
