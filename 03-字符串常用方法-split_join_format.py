# 1. split()  切割 ***
# 2. join()   将序列中的元素以指定的字符连接生成一个新的字符串 ***
# 3. format() 格式化输出 ***


# 例题1：split()
# s1 = 'libai_and_dufu_and_wangwei'
# s2 = s1.split('_')
# print(s1)
# print(s2)

# s1 = '_libai_and_dufu_and_wangwei_'
# s2 = s1.split('_')
# print(s1)
# print(s2)

# s1 = 'libai__and_dufu_and_wangwei'
# s2 = s1.split('_')
# print(s1)
# print(s2)

# s1 = 'libai___and_dufu_and_wangwei'
# s2 = s1.split('_')
# print(s1)
# print(s2)


# 例题2：join()
# lst1 = ['李白', '杜甫', '王维', '白居易', '李商隐', '杜甫']
# s = '_'.join(lst1)
# print(s)


# 例题3：format()
# name1 = '李白'
# name2 = '太白'
# year = 701
# poem = '静夜思'
# s1 = '{}，字{}，{}年出生，《{}》'.format(name1, name2, year, poem)
# print(s1)

# name1 = '李白'
# name2 = '太白'
# year = 701
# poem = '静夜思'
# s1 = '{a}，字{b}，{c}年出生，《{d}》'.format(c=year, d=poem, a=name1, b=name2)
# print(s1)
