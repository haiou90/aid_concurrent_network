"""
空洞文件
"""

f = open("file.txt",'wb')

f.write(b"begin")
f.seek(100000,2)
f.write(b'end')

f.close()