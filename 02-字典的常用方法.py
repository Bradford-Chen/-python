# 1. keys()   返回所有的key
# 2. values() 返回所有的value
# 3. items()  返回键值对，元组
# 4. len()    计算字典元素个数


# 例题1：keys()
# dic = {'静夜思': '李白', '登高': '杜甫', '长恨歌': '白居易'}
# print(dic)
# a = dic.keys() # 拿到所有的key，返回key的集合，像是列表，但是不是列表
# print(a)
# b = list(dic.keys())
# print(b)

# dic = {'静夜思': '李白', '登高': '杜甫', '长恨歌': '白居易'}
# for key in dic.keys():  # 可以进行迭代循环
#     print(key)

# 例题2：values()
# dic = {'静夜思': '李白', '登高': '杜甫', '长恨歌': '白居易'}
# a = dic.values()
# print(a)
# b = list(dic.values())
# print(b)

# dic = {'静夜思': '李白', '登高': '杜甫', '长恨歌': '白居易', '蜀道难': '李白'}
# a = dic.values()
# print(a)
# b = list(dic.values())
# print(b)

# 例题3：items()
# dic = {'静夜思': '李白', '登高': '杜甫', '长恨歌': '白居易'}
# a = dic.items()
# print(a)
# b = list(dic.items())
# print(b)

# dic = {'静夜思': '李白', '登高': '杜甫', '长恨歌': '白居易'}
# for item in dic.items():
#     print(item)
#     key, value = item
#     print(key)
#     print(value)

# dic = {'静夜思': '李白', '登高': '杜甫', '长恨歌': '白居易'}
# for key, value in dic.items():
#     print(key)
#     print(value)
#     print()

# 例题4：计算字典里的元素
dic = {'静夜思': '李白', '登高': '杜甫', '长恨歌': '白居易'}
num = len(dic)
print(num)