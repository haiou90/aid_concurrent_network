"""
套接字函数基础展示
"""
import socket

# 创建一个udp套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# udp_socket.bind(('0.0.0.0',8888))

# udp_socket.bind(('127.0.0.1',8888))
# udp_socket.bind(('localhost',8888))

udp_socket.bind(('172.40.0.228',8888))

