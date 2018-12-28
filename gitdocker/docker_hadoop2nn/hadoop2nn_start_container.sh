echo "start hadoop-2ndnamenode container..."
docker run -itd --restart=always \
                --net=host  \
                --privileged  \
                --name dkr_hadoop2namenode  \
                --hostname hadoop2nn dkr_hadoop2nn  /usr/sbin/init

echo start sshd...
#docker exec -it hadoop2nn sh ~/start-hadoop-daemon.sh
docker exec -t -i dkr_hadoop2namenode sh hadoop-daemon.sh start secondarynamenode
docker exec -t -i dkr_hadoop2namenode sh hadoop-daemon.sh start datanode

echo finished
docker ps
