# range() 函数可创建一个整数列表，一般用在 for 循环中
# 一个参数: 0开始，结束为止，步长为1
# 两个参数: 1起始位置，2结束位置
# 三个参数: 1起始位置，2结束位置，3步长


# 例题1：
# a = range(10)
# print(a)
# b = list(a)
# print(b)


# 例题2：
# for i in range(10):
#     print(i)

# for i in range(3, 10):
#     print(i)

# for i in range(3, 10, 2):
#     print(i)

# for i in range(10, 3, -1):
#     print(i)


# 例题3：通过索引依次取出列表元素
# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# for item in lst1:
#     print(item)

# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# for item in range(len(lst1)):
#     print(lst1[item])

# 例题4：
lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
lst2 = ['静夜思', '登高', '相思', '长恨歌', '无题']
result = []
for item in range(len(lst1)):
    data = [lst1[item], lst2[item]]
    print(data)
    result.append(data)
print(result)

