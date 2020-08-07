import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto(b'nihao',('127.0.0.1',8888))

data,client_addr = s.recvfrom(1024)
print(data)

s.close()