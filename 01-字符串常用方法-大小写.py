# 1. upper() 全部大写
# 2. lower() 全部小写
# 3. capitalize() 将字符串的第一个字母变成大写，其他字母变小写
# 4. title() 所有单词都是以大写开始，其余字母均为小写

# 字符串是一个不可变对象

# 例题1：upper() lower()
# s1 = 'libai and dufu and wangwei'
# s2 = s1.upper()
# print(s1)
# print(s2)

# s1 = 'Libai and DUFU and wangwei'
# s2 = s1.lower()
# print(s1)
# print(s2)


# 例题2：输入验证码（不区分大小）
# code = input('请输入验证码')
# print('您输入的验证码是：%s' % code)
# if code.lower() == 'agtf':
#     print('验证码通过')
# else:
#     print('验证码没有通过')


# 例题3：capitalize()
# s1 = 'the libai And dufu And wangwei'
# s2 = s1.capitalize()
# print(s1)
# print(s2)

# s1 = ' the libai And dufu And wangwei' # 前面有空格
# s2 = s1.capitalize()
# print(s2)

# 例题4：title()
# s1 = 'libai and dufu and wangwei'
# s2 = s1.title()
# print(s2)

# s1 = 'libai and dufu and-wangwei'
# s2 = s1.title()
# print(s2)
