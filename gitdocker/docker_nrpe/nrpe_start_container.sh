echo start nrpe_2 container...
docker run -itd --restart=always --net=host \
                --privileged \
                --name dkr_nrpe_2_run \
                --hostname nrpe_2-run \
                dkr_nrpe_2  /usr/sbin/init



echo start sshd...
docker exec -it dkr_nrpe_2_run systemctl start sshd




echo finished
docker ps

