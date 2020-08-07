import socket

host = '127.0.0.1'
port = 8888
addr = (host,port)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(addr)

data,client_addr = s.recvfrom(1024)
print('recvfrom addr',client_addr)
print(data)

s.sendto(b'ok',client_addr)

s.close()

