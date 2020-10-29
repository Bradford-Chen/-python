# 1.  strip()  去掉字符串两边空格 ***
# 2.  lstrip() 去掉字符串左边空格
# 3.  rstrip() 去掉字符串右边空格
# 4.  replace() 替换 ***


# 例题1：strip() lstrip() rstrip()
# s1 = '  libai and dufu and wangwei  '
# s2 = s1.strip()
# print('|%s|' % s1)
# print('|%s|' % s2)

# s1 = '  libai and dufu and wangwei  '
# s2 = s1.lstrip()
# print('|%s|' % s1)
# print('|%s|' % s2)

# s1 = '  libai and dufu and wangwei  '
# s2 = s1.rstrip()
# print('|%s|' % s1)
# print('|%s|' % s2)

# 例题2：输入账号和密码
usename = input('请输入账号：').strip()
password = input('请输入密码：').strip()
if usename == 'ray' and password == '123':
    print('验证通过')
else:
    print('账号和密码错误')

# 例题3：replace()
# s1 = 'libai and dufu and wangwei and dufu and dufu'
# s2 = s1.replace('dufu', '杜甫')
# print(s2)

# s1 = 'libai and dufu and wangwei and dufu and dufu'
# s2 = s1.replace('dufu', '杜甫', 20)
# print(s2)

# s1 = 'libai and dufu and wangwei and dufu and dufu'
# s2 = s1.replace('gw', '杜甫')
# print(s2)

# s1 = 'libai and dufu and wangwei and dufu and dufu'
# s2 = s1.replace('gk', '杜甫')
# print(s2)

# s1 = 'libai and dufu and wangwei and dufu and dufu'
# s2 = s1.replace(' ', '')
# print(s2)
