import string

a = "Hi"
print(isinstance(a, str))


"""是否是数字、字母、大小写 空白符"""
"""
a.isalnum()
a.isalpha()
a.isdigit()
a.islower()
a.isupper()
a.startswith()
a.endswith()
"""
# assert "Hello word".istitle() == True


"""查找与替换"""

# 返回字符串S [start：end]中子字符串sub的不重叠出现的次数。 可选参数start和end的解释方式为切片表示法
a = "11111wd3ewdmfjojp43285ipfsojdfsfposdjfl;jdsofjsodf"
print(a.count("1"))

str_data = "Test if a string contains some special substrings"
print(str_data.find("some"))
new_str = str_data.replace("e","$", 2)
print(str_data)
print(new_str)
print(" hello word  1 1111  ".split())
# ['hello', 'word', '1', '1111']
# 先去除两端空白以任意长度的空白符分隔
print(" hello word  1 1111  ".split(' '))
#['', 'hello', 'word', '', '1', '1111', '', '']
ret = string.capwords(' hello    world   ')
print(ret)
# 清楚两端空白字符 再将连续的空白符用空格代替

ret = 'a hello    world    '.strip()
# 去除空白字符  由 string.whitespace 常量定义
print(ret)

