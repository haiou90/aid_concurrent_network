"""
文件打开方式示例
"""

# 打开文件  读方式打开文件必须存在
# f = open("/home/tarena/Month01/exercise01.py","r")

# 写方式打开 文件内容清空
# f = open("file.txt",'w')

# 追加方式  文件不清除
f = open("file.txt",'a')

# 操作文件读写
print(f)

# 关闭文件
f.close()