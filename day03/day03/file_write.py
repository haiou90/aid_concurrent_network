"""
文件写操作示例
"""

# 写方式打开
# f = open("file.txt","w")

# f = open("file.txt","a") # 追加

# 读写方式打开，写入文本会从头开始往后覆盖内容
# f = open("file.txt","r+")

f = open("file.txt",'w')

# 写入操作了
n = f.write("Hello world\n")
print("写入了 %d 个字节"%n)
n = f.write("Hello Kitty\n")
print("写入了 %d 个字节"%n)

# 将列表中的内容分别写入到文件中
l = ["哈喽，死鬼\n","哎呀，干啥\n"]
f.writelines(l)

# 关闭
f.close()