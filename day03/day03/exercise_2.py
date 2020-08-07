"""
重点代码！！

练习2： 文件的复制
下载一个图片（二进制文件），将这个文件下载到主目录
编写程序，将这个文件复制到当前程序所在目录中

提示： 从原文件读内容，写到新文件
      不允许一次性读取所有内容
"""
# 打开源文件
fr = open("/home/tarena/timg.jfif",'rb')
fw = open("timg.jfif",'wb')

# 循环读写内容
while True:
    # 一边读取，一边写入
    data = fr.read(1024)
    if not data:
        break
    fw.write(data)

# 关闭文件
fr.close()
fw.close()
