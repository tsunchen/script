from socket import *
import time

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(('localhost', 5001))
tcp_server.listen(5)
print ("wait client")
client, client_info = tcp_server.accept()
recv_data = client.recv(1024)
print (recv_data)

client.close()
tcp_server.close()
