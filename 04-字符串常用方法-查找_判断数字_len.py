# 1. startswith() 判断是否以xxx开头
# 2. endswith()   判断是否以xxx结尾
# 3. count()      统计字符串里某个字符出现的次数 *
# 4. find()  查找，如果找不到返回-1
# 5. index() 查找，如果找不到会报错

# 6. isalpha()    方法检测字符串是否只由字母组成
# 7. isdigit()   方法检测字符串是否只由数字组成
# 8. isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象

# 9. len() 求字符串的长度。内置函数，直接使用，不用点操作 ***


# 例题1：startswith() endswith()
# s1 = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
# b = s1.startswith('床')
# print(b)

# s1 = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
# b = s1.startswith('船')
# print(b)

# s1 = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
# b = s1.endswith('。')
# print(b)

# s1 = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
# b = s1.endswith('.')
# print(b)

# 例题2：count()
# s1 = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
# num = s1.count('头')
# print(num)


# 例题3：find()
# s1 = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
# s2 = s1.find('是')
# print(s2)

# s1 = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
# s2 = s1.find('后')
# print(s2)

# 例题4：index()
# s1 = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
# s2 = s1.index('是')
# print(s2)

# s1 = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
# s2 = s1.index('后')
# print(s2)

# 例题5：isalpha() isdigit() isnumeric()
# s1 = '123'
# b = s1.isalpha()
# print(b)

# s1 = '123a'
# b = s1.isalpha()
# print(b)

# s1 = 'abc'
# b = s1.isalpha()
# print(b)

# s1 = '123'
# b = s1.isdigit()
# print(b)

# s1 = '123a'
# b = s1.isdigit()
# print(b)

# s1 = '12.3'
# b = s1.isdigit()
# print(b)

# s1 = '二千136万萬贰'
# b = s1.isnumeric()
# print(b)

# s1 = '二千136万萬两'
# b = s1.isnumeric()
# print(b)


# 例题6：len()
# s1 = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
# num = len(s1)
# print(num)