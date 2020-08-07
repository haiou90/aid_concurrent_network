"""
字节串类型演示  bytes

* 所有字符串都能转换为字节串
* 并不是所有的字节串都能转换为字符串
"""

# 定义一个字节串数据
b1 = b"hello world"  # 英文字符
print(type(b1))

b2 = "你好".encode() # utf8字符定义为字节串
print(b2)

s = "hello ,死鬼"
b3 = s.encode() # 变量使用encode转换
print(b3)

# 字节串转换为字符串
print("转换为字符串：",b'hello ,\xe7\xcd\xfb\xe9\xac\xbc'.decode())


