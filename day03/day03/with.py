"""
with语句块 打开文件
"""

# 生成f
with open('file.txt','rb+') as f:
    data = f.read(5)
    print(data.decode())
    f.write(b"hahahaha")

# 语句块结束会自动销毁 f