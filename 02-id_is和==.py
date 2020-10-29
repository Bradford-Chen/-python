# id() 函数返回对象的唯一标识符，标识符是一个整数

# 例题1：
# s1 = '李白'
# a1 = id(s1)
# print(a1)

# s1 = '李白'
# s2 = '李白'
# print(id(s1))
# print(id(s2))

# 小数据池，会对字符串进行缓存，为了节省内存
# s1 = '李白'*10000
# s2 = '李白'*10000
# print(id(s1))
# print(id(s2))


# 例题2
# a = True
# b = True
# print(id(a))
# print(id(b))


# is 判断的是内存地址，根据id()的值来判断，也就是内存地址
# == 左右两端是否相等和一致，比较的是内容


# 例题3：
# lst1 = ['李白', '杜甫']
# lst2 = ['李白', '杜甫']
# print(id(lst1))
# print(id(lst2))
# a = lst1 == lst2
# print(a)
# b = lst1 is lst2
# print(b)
import requests