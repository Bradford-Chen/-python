# %s 字符串的占位符, 可以放置任何内容(数字)
# %d 数字的占位符


# 例题1：
# print('李白，字太白，701年出生，《静夜思》')
# print('杜甫，字子美，712年出生，《登高》')
# print('王维，字摩诘，701年出生，《九月九日忆山东兄弟》')

# name1 = input('请输入名字：')
# name2 = input('请输入字：')
# year = input('请输入出生年：')
# poem = input('请输入诗词：')
# s1 = name1 + '，字' + name2 + '，' + year + '年出生，《' + poem + '》'
# print(s1)


# 例题2：
# name1 = input('请输入名字：')
# name2 = input('请输入字：')
# year = input('请输入出生年：')
# poem = input('请输入诗词：')
# s1 = '%s，字%s，%s年出生，《%s》' % (name1, name2, year, poem)
# print(s1)

# name = '李白'
# s1 = '人：%s' % (name)
# print(s1)

# name = '李白'
# year = '701'
# s1 = '人：%s；年龄：%s' % (name, year)
# print(s1)

# 例题3：
# a = 300
# s = '唐诗%d首' % a
# print(s)

# a = '300'
# s = '唐诗%d首' % a
# print(s)

# a = 300
# s = '唐诗%s首' % a
# print(s)


# 例题4：
# 如果字符串中有了占位符，那么后面的所有的%都是占位，需要转义
name = '李白'
# s = '%s很有才华，唐诗300收的50%的诗词都是他的' % name
# print(s)
s = '%s很有才华，唐诗300收的50%的诗词都是他的'
print(s)
