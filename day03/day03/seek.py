"""
文件偏移量演示
"""

f = open("file.txt",'wb+')

f.write(b"Hello world\n")
f.flush()


f.seek(-2,2) # 从结尾向前移动2字节
print("当前文件偏移量位置:",f.tell())

data = f.read() # 从文件偏移量所在位置读
print(data)

f.close()