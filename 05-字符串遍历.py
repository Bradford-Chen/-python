# 把字符串从头到尾进行遍历

# 方法1：while循环
# s = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
# num = len(s)
# count = 0
# while count < num:
#     print(s[count])
#     count = count + 1

# 方法2：for循环
# for i in s:
#     print(i)


# 方法3：for循环
# s1 = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
# s2 = '渡远荆门外，来从楚国游。山随平野尽，江入大荒流。'
# num = len(s1)
# lst = range(num)
# print(lst)
# print(list(lst))
# for i in lst:
#     print(s1[i], s2[i])

# s1 = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
# s2 = '渡远荆门外，来从楚国游。山随平野尽，江入大荒流。'
# for i in range(len(s1)):
#     print(s1[i], s2[i])
