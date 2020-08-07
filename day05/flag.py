"""
re模块功能扩展标志
"""
import re

# 目标字符串
s = """Hello
北京
"""
# # 让正则表达式只能匹配ascii码（英文符号）
# l = re.findall(r"\w+", s, flags=re.A)
# print(l)
#
# # 让 . 可以匹配换行
# l = re.findall(r".+", s, flags=re.S)
# print(l)
#
# # 忽略字母大小写
# l = re.findall(r"[a-z]+", s,flags=re.I)
# print(l)

# 让^ $ 可以匹配每一行的开头结尾位置
l = re.findall(r"\w+$", s,flags=re.M)
print(l)

