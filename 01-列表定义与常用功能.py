# 1. 列表的定义
# 2. 列表的索引和切片
# 3. 列表元素的增加
#      append() ***
#      extend() ***
#      insert()
# 4. 列表元素的删除
#      pop()
#      remove()
#      del
# 5. 列表元素的查询
# 6. 列表元素的修改
# 7. len() ***
# 8. sort()    # 排序 ***
# 9. sorted()  # 排序 ***


# 例题1：定义
# lst1 = ['李白', '杜甫', '王维']
# print(lst1)

# lst1 = [666, True, '王维']
# print(lst1)

# lst1 = ['李白', '杜甫', '王维', ['唐诗', '宋词']]
# print(lst1)

# 例题2：列表的索引和切片
# 列表的索引和切片，与字符串一样
# lst1 = ['李白', '杜甫', '王维', ['唐诗', '宋词']]
# print(lst1[1])
# print(lst1[-1][1])


# 例题3：列表元素的增加：append()
# lst1 = ['李白', '杜甫', '王维']
# lst1.append('白居易')
# print(lst1)
# lst1.append('李商隐')
# print(lst1)

# append() 没有返回值
# lst1 = ['李白', '杜甫', '王维']
# lst2 = lst1.append('白居易')
# print(lst1)
# print(lst2)

# lst1 = ['李白', '杜甫', '王维']
# lst1.append(['唐诗', '宋词'])
# print(lst1)

# lst1 = ['李白', '杜甫', '王维']
# lst1.extend(['唐诗', '宋词'])
# print(lst1)

# 例题4：列表元素的增加：insert()
# lst1 = ['李白', '杜甫', '王维']
# lst1.insert(1, '白居易')
# print(lst1)

# 例题5：
# lst = []
# while 1:
#     name = input('请输入学生名字')
#     if name == 'q':
#         break
#     else:
#         lst.append(name)
#         print(lst)
# print(lst)

# 例题6：列表元素的删除：pop()
# 删除最后一个，并返回所删除的元素
# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# e = lst1.pop()
# print(lst1)
# print(e)

# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# e = lst1.pop(2)
# print(lst1)
# print(e)

# 例题7：列表元素的删除：remove()
# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# lst1.remove('杜甫')
# print(lst1)

# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# e = lst1.remove('杜甫')
# print(lst1)
# print(e)

# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# lst1.remove('杜牧')
# print(lst1)

# lst1 = ['李白', '杜甫', '王维', '杜甫', '白居易', '李商隐', '杜甫']
# lst1.remove('杜甫')
# print(lst1)

# lst1 = ['李白', '杜甫', '王维', '杜甫', '白居易', '李商隐', '杜甫']
# lst1.remove('杜甫')
# lst1.remove('杜甫')
# lst1.remove('杜甫')
# print(lst1)

# 例题8：列表元素的删除：del
# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# del lst1[1]
# print(lst1)

# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# del lst1[1:4]
# print(lst1)


# 例题9：列表元素的删除：clear()
# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# lst1.clear()
# print(lst1)


# 例题11：列表元素的查询：遍历全部元素
# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# for item in lst1:
#     print(item)

# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# for item in range(len(lst1)):
#     print(lst1[item])


# 例题12：列表元素的查询：根据值来查询
# lst1 = ['李白', '杜甫', '王维', '杜甫', '白居易', '李商隐', '杜甫']
# num = lst1.count('杜甫')
# print(num)

# lst1 = ['李白', '杜甫', '王维', '杜甫', '白居易', '李商隐', '杜甫']
# num = lst1.count('杜牧')
# print(num)

# 例题13：列表元素的修改：索引
# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# lst1[1] = '杜牧'
# print(lst1)


# 例题14：获得列表元素的个数
# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
# num = len(lst1)
# print(num)

# lst1 = ['李白', '杜甫', '王维', ['唐诗', '宋词']]
# num = len(lst1)
# print(num)


# 例题15：排序
# lst1 = [1, 9, 18, 2, 34, 88, 7, 9]
# lst1.sort()
# print(lst1)

# lst1 = [1, 9, 18, 2, 34, 88, 7, 9]
# lst2 = lst1.sort()
# print(lst1)
# print(lst2)

# lst1 = [1, 9, 18, 2, 34, 88, 7, 9]
# lst2 = sorted(lst1)
# print(lst1)
# print(lst2)

# 排序的规则，是按照拼音排吗？否
lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐']
lst1.sort()
print(lst1)
