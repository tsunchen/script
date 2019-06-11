from socket import *

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(('localhost', 5001))
str = "pythonask chaosworld"
tcp_client.send(str.encode())
tcp_client.close()
