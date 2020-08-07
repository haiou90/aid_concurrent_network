import socket
from multiprocessing import Process
from signal import *
import sys

host = '127.0.0.1'
port = 8888
addr = (host,port)

def handle(cli_sock):
    while True:
        data = cli_sock.recv(1024)
        print(data)
        # strip()去除字符串两端的空白字符
        if data.strip() == b'end':
            break
        cli_sock.send(b'ok')
    cli_sock.close()

def main():
    s = socket.socket()
    # 设置套接字地址重用 设置套接字选项SOL_SOCKET的值为SO_REUSEADDR
    # 程序结束之后可以立即在原地址运行
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)

    signal(SIGCHLD,SIG_IGN)
    # 20:06~20:20
    while True:
        try:
            cli_sock, cli_addr = s.accept()
            print('Client connect from', cli_addr)
        except KeyboardInterrupt as e:
            s.close()
            sys.exit('服务器退出')

        p = Process(target=handle,args=(cli_sock,))
        p.daemon = True
        p.start()


if __name__ == '__main__':
    main()