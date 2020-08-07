import socket


c = socket.socket()
c.connect(('127.0.0.1',8888))

while True:
    data = input('>>>')+'\r\n'
    c.send(data.encode('utf8'))
    if data.strip() == 'end':
        print('客户端结束通信')
        break

    print(c.recv(1024))

c.close()