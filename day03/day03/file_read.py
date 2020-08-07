"""
文件读取 示例
"""

# 打开文件
f = open("file.txt",'r')

# 读取文件内容
# data = f.read() # 不加参数表示获取文件所有内容
# print("读取到的内容:",data) # 二进制读取字节串

# 对于大文件通常都会分块循环读取
# while True:
#     data = f.read(1024)
#     # 读取到文件结尾继续读取则会得到空字符串
#     if not data:
#         break
#     print(data,end='')

# 读取一行内容

# 读取到10个字符或者遇到换行都会终止读取
# data = f.readline(10)
# print("一行内容:",data)
# data = f.readline()
# print("一行内容:",data)

# 读取多行内容 文件每一行读取为列表中一个元素
# data_list = f.readlines(62)
# print(data_list)

# 迭代获取
for line in f:
    print(line,end='') # 每次获取一行

# 关闭文件
f.close()