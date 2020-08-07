"""
练习1：使用input输入一个单词，打印出这个单词的解释
，如果没有这个单词则打印"没有找到该单词"

提示：
    * 每个单词占一行
    * 单词与解释之间有空格
    * 单词按照从小到大排列
"""

# 输入一个单词
word = input("Word:")

f = open("dict.txt") # 默认就是读

# 查找单词
for line in f:
    w = line.split(' ',2)
    if w[0] > word:
        # 遍历到的单词已经大于目标就没必要继续找了
        print("没有该单词")
        break
    elif word == w[0]:
        # 找到单词 打印
        # print(w[-1].strip())
        print(line)
        break # 结束查找
else:
    print("没有找到该单词")

f.close()