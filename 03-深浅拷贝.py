# 例题1：
# lst1 = ['李白', '杜甫', '王维']
# lst2 = lst1  # 进行赋值操作，实际上是引用内存地址的赋值，内存中此时只有一个列表，两个变量指向一个列表
# lst2.append('白居易')  # 对其中的一个进行操作，两个都跟着变
# print(id(lst1), lst1)
# print(id(lst2), lst2)


# 例题2：
# 浅拷贝 copy 创建新对象
# 方法1
lst1 = ['李白', '杜甫', '王维']
lst2 = lst1.copy()  # lst2 和 lst1 不是同一个对象
lst1.append('白居易')
print(id(lst1), lst1)
print(id(lst2), lst2)

# 方法2
# lst1 = ['李白', '杜甫', '王维']
# lst2 = lst1[:]  # 切片会产生新的对象
# lst1.append('白居易')
# print(id(lst1), lst1)
# print(id(lst2), lst2)


# 例题3：
# lst1 = ['李白', '杜甫', '王维', ['唐诗', '宋词']]
# lst2 = lst1.copy()  # 浅拷贝，拷贝第一层
# lst1[3].append('元曲')
# print(id(lst1), lst1)
# print(id(lst2), lst2)
# print(id(lst1[0]), id(lst2[0]))
# print(id(lst1[3]), id(lst2[3]))


# 例题4：
# 深拷贝
# import copy
# lst1 = ['李白', '杜甫', '王维', ['唐诗', '宋词']]
# lst2 = copy.deepcopy(lst1)  # 把lst1扔进去进行深度拷贝，包括内部的所有内容进行拷贝
# lst1[3].append('元曲')
# print(id(lst1), lst1)
# print(id(lst2), lst2)
#
# print(id(lst1[0]), id(lst2[0]))
# print(id(lst1[3]), id(lst2[3]))


# 为什么要有深浅拷贝
# 拷贝比创建对象的过程要快

