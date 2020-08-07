"""
缓冲区演示
"""

#  行缓冲
# f = open('file.txt','w',buffering=1)

# 指定缓冲区大小
f = open('file.txt','wb',buffering=10)

# 循环写入内容
while True:
    info = input(">>")
    if not info:
        break
    f.write(info.encode())
    # f.flush() # 主动刷新缓冲区

f.close()