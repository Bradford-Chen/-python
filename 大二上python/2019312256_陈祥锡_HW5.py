# 陈祥锡 信管19-1 2019312256
# 2020/10/27
import math


def main():
    n = int(input("请输入一个整数n："))
    a1 = 1
    a2 = 0
    for i in range(n):
        a = a1 + a2
        a1 = a2
        a2 = a
    print("第n个斐波那契数为：%d" % a)


main()

####

def main():
    n = int(input("请输入一个大于2的整数："))
    for i in range(2, math.sqrt(n) + 1):
        if n % i == 0:
            break
    print