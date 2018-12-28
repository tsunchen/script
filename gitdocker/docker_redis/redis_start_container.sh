echo start redis container...
docker run -itd --restart=always --net=host \
                --privileged \
                --name dkr_redis_run \
                --hostname redis-run \
                dkr_redis  /usr/sbin/init



echo start sshd...
docker exec -it dkr_redis systemctl start sshd

docker exec -d  dkr_redis sh /root/init_redis.sh



echo finished
docker ps

