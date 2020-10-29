# 元组
# 有索引和切片。
# 不可变对象。不可变的是它内部子元素。如果子元素是列表，则列表的元素是可以变的。


# 例题1：
# tup1 = ('李白', '杜甫', '王维', '白居易', '李商隐')
# print(tup1)
# print(type(tup1))

# tup1 = (1)
# print(tup1)
# print(type(tup1))

# tup1 = ('1')
# print(tup1)
# print(type(tup1))

# tup1 = (1,)
# print(tup1)
# print(type(tup1))

# tup1 = ('1',)
# print(tup1)
# print(type(tup1))


# 例题2：读取元素
# tup1 = ('李白', '杜甫', '王维', '白居易', '李商隐')
# print(tup1[1])

# tup1 = ('李白', '杜甫', '王维', '白居易', '李商隐')
# print(tup1[1:3])

# 例题3：
# tup1 = ('李白', '杜甫', '王维', '白居易', '李商隐')
# tup1[1] = '杜牧' # 不能改，会报错

# 例题4：
# tup1 = ('李白', '杜甫', '王维', ['唐诗', '宋词'])
# tup1[-1].append('元曲') # 元组本身没有变. 变的是儿子中的内容
# print(tup1)